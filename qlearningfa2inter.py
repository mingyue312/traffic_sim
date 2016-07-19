import random
import numpy as np
import copy

SATable = []
n = 0
flag = 0
prev_state = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
prev_action = {(1,1):1, (1,2):1}
list_of_actiontodict = ["null",{(1,1):0, (1,2):0}, {(1,1):0, (1,2):1}, {(1,1):1, (1,2):0}, {(1,1):1, (1,2):1}]
a = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
theta = np.array( a )

def lane_threshold(a):
    "convert car length in a lane into thresholds 1-short 2-intermediate 3-long"
    if a <= 5:
        return 1
    elif (a > 5 and a < 12):
        return 2
    elif (a >= 12):
        return 3

def fa_lane_threshold(a):
    "convert car length in a lane into thresholds 1-short 2-intermediate 3-long"
    if a <= 5:
        return 0
    elif (a > 5 and a < 12):
        return 0.5
    elif (a >= 12):
        return 1

def time_threshhold(a):
    "convert time signal has been red into thresholds 1-short 2-intermediate 3-long"
    if a <= 4:
        return 1
    elif (a > 4 and a <= 8):
        return 2
    elif (a > 8):
        return 3

def fa_time_threshhold(a):
    "convert time signal has been red into thresholds 1-short 2-intermediate 3-long"
    if a <= 6:
        return 0
    else:
        return 1

def ObserveState(state_array):
    "Given a state array - [number of cars in westr, westl, ..., eastl, eastr, red time, signal1,] return the state ID"
    lane1 = max(state_array[0], state_array[1])
    lane2 = max(state_array[2], state_array[3])
    lane3 = max(state_array[4], state_array[5])
    lane4 = max(state_array[6], state_array[7])
    time = state_array[8]
    state = [lane_threshold(lane1), lane_threshold(lane2), lane_threshold(lane3), lane_threshold(lane4), \
             time_threshhold(time)]
    return state

def fa_ObserveState(state_array):
    "Given a state array - [number of cars in westr, westl, ..., eastl, eastr, red time, signal1,] return the state ID"

    lane1 = max(state_array[0], state_array[1])
    lane2 = max(state_array[2], state_array[3])
    lane3 = max(state_array[4], state_array[5])
    lane4 = max(state_array[6], state_array[7])
    time = state_array[8]
    state = [fa_lane_threshold(lane1), fa_lane_threshold(lane2), fa_lane_threshold(lane3), fa_lane_threshold(lane4), \
             fa_time_threshhold(time)]
    return state

def lanelights (int):
    if int == 1:
        return [1,1,0,0]
    else:
        return [0,0,1,1]

def fa_merge(state1, state2):
    global prev_action
    sigma = state1[0:4]+state2[0:4]+state1[4:5]+state2[4:5]+lanelights(prev_action[(1,1)])+ lanelights(prev_action[(1,2)])
    return sigma

def findindex(state):
    "Given the state ID returns state index in the SATable"
    index = 0
    for i in range(0, 10):
        index += (3 ** (9 - i)) * (state[i] - 1)
    return index


def reward(state1, state2):
    "Started in state1 action was taken to get to state2, calculates a reward used in Q-Learning formula"
    a = 1
    b = 1
    c = 0
    sumlanelength1 = 0
    sumlanelength2 = 0
    sumtime1 = 0
    sumtime2 = 0
    while c < 9:
        for i in range(c, c+4): #0,1,2,3 (0-4), 5,6,7,8 (5-9)
            sumlanelength1 += state1[i]
            sumlanelength2 += state2[i]
        sumtime1 += state1[c+4]
        sumtime2 += state2[c+4]
        c += 5
    reward = a * (sumlanelength1 - sumlanelength2) + b * (sumtime1 - sumtime2)
    return reward

def fa_cost(state1):
    a = 0.5
    b = 0.5
    sumlanelength = sum(state1[0:8])
    sumtime = 2*(state1[8] + state1[9])
    cost = a*(sumlanelength) + b*(sumtime)
    return cost



def UpdateQvalue(state1, state2, action):
    "Updates Q-Value for a given state-action pair in the SATable based on Q-Learning formula"
    #e.g state = [1,2,3,1,2,3,1,2,3,1]
    #from state1 action was taken to get to state2
    global SATable
    global n
    global flag
    index1 = findindex(state1)
    index2 = findindex(state2)
    alpha = (1/float(n))
    gamma = 0.9
    localoldqvalue = SATable[index1][action]
    SATable[index1][action] = round(((1 - alpha) * (SATable[index1][action]) + alpha * (reward(state1, state2) + \
                                  gamma * (max(SATable[index2][1], SATable[index2][2], SATable[index2][3], SATable[index2][4])))),10)
    localnewqvalue = SATable[index1][action]
    if (n>20000):
        flag = 1
    extraline = 1

def UpdateQvaluefa(ps, cur_state):
    #ps -> prev_state
    global theta
    global n
    global flag
    #cur_state is equal to sigma in the literture
    alpha = 1/(float(n**0.51))
    gamma = 0.9
    cost = fa_cost(ps)
    statecopy = copy.deepcopy(cur_state)
    action_with_minqvalue = -1
    min_q_value = 9999999999
    for actionindex in range(1,5):
        statecopy[10:18] = lanelights(list_of_actiontodict[actionindex][(1,1)])+lanelights(list_of_actiontodict[actionindex][(1,2)])
        q_value = np.dot(theta, np.array(statecopy))
        if q_value <= min_q_value:
            min_q_value = q_value
            action_with_minqvalue = actionindex
    statecopy [10:18] = lanelights(list_of_actiontodict[action_with_minqvalue][(1,1)])+lanelights(list_of_actiontodict[action_with_minqvalue][(1,2)])
    sigmacur = np.array( statecopy )
    sigmapast = np.array( ps )
    theta = theta + alpha*sigmapast*( cost + gamma*(np.dot(theta,sigmacur) - np.dot(theta, sigmapast)))
    if (n > 20000):
        flag = 1
    extraline = 1



def takeAction(state1):
    "Decide which action to take based on optimal Q-Value with epsilon greedy algorithm"
    global SATable
    a = random.random()
    if a <= 0.65:
        stateindex = findindex(state1)
        indexmax = 1 #index of action with max qvalue
        indexsame = [] #list of indices with same max qvalue
        for i in range (2,5):
            if SATable[stateindex][i] > SATable[stateindex][indexmax]:
                indexmax = i
                indexsame = []
            if SATable[stateindex][i] == SATable[stateindex][indexmax]:
                indexsame.append(i)
        if indexsame != []: # if indexsame == [] means that indexmax is only max qvalue
            indexsame.append(indexmax)
            randomindex = random.randint(0,len(indexsame)-1)
            return indexsame[randomindex]
        else:
            return indexmax
    else:
        actionindex = random.randint(1,4)
        return actionindex

def fa_takeAction(state):
    global theta
    global list_of_actiontodict
    a = random.random()
    if a <= 0.65:
        statecopy = copy.deepcopy(state)
        action_with_minqvalue = -1
        min_q_value = 9999999999
        for actionindex in range(1,5):
            statecopy[10:18] = lanelights(list_of_actiontodict[actionindex][(1,1)])+lanelights(list_of_actiontodict[actionindex][(1,2)])
            q_value = np.dot(theta, np.array(statecopy))
            if q_value <= min_q_value:
                min_q_value = q_value
                action_with_minqvalue = actionindex
        return action_with_minqvalue
    else:
        actionindex = random.randint(1, 4)
        return actionindex

def fa_actionoptimal(state):
    global theta
    global list_of_actiontodict
    statecopy = copy.deepcopy(state)
    action_with_minqvalue = -1
    min_q_value = 9999999999
    for actionindex in range(1,5):
        statecopy[10:18] = lanelights(list_of_actiontodict[actionindex][(1,1)])+lanelights(list_of_actiontodict[actionindex][(1,2)])
        q_value = np.dot(theta, np.array(statecopy))
        if q_value <= min_q_value:
            min_q_value = q_value
            action_with_minqvalue = actionindex
    return action_with_minqvalue

def takeActionoptimal(state):
    global SATableoptimal
    stateindex = findindex(state)
    indexmax = 1 #index of action with max qvalue
    indexsame = [] #list of indices with same max qvalue
    for i in range (2,5):
        if SATable[stateindex][i] > SATable[stateindex][indexmax]:
            indexmax = i
            indexsame = []
        if SATable[stateindex][i] == SATable[stateindex][indexmax]:
            indexsame.append(i)
    if indexsame != []: # if indexsame == [] means that indexmax is only max qvalue
        indexsame.append(indexmax)
        randomindex = random.randint(0,len(indexsame)-1)
        return indexsame[randomindex]
    else:
        return indexmax

def optimalaction(state_dict):
    state1 = ObserveState(state_dict[(1,1)]) #find state id of inter(1,1)
    state2 = ObserveState(state_dict[(1,2)]) #find state id of inter(1,2)
    cur_state = state1 + state2
    action = takeActionoptimal(cur_state)
    # temp = SATableoptimal[findindex(cur_state)]
    return action

def qlearning(state_dict):
    global SATable
    global SATableoptimal
    global prev_state
    global prev_action
    global n
    global flag
    if (flag == 0):
        state1 = ObserveState(state_dict[(1,1)]) #find state id of inter(1,1)
        state2 = ObserveState(state_dict[(1,2)]) #find state id of inter(1,2)
        n += 1
        cur_state = state1 + state2
        actionindex = takeAction(cur_state)
        action = list_of_actiontodict[actionindex]
        if n != 1:
            UpdateQvalue(prev_state, cur_state, prev_action)
        prev_state = cur_state
        prev_action = actionindex
        return action
    elif (flag == 1):
        if SATableoptimal == []:
            SATableoptimal = SATable
        actionindex = optimalaction(state_dict)
        action = list_of_actiontodict[actionindex]
        return action

def qlearningfa(state_dict):
    global flag
    global n
    global prev_action
    global prev_state
    sigma = fa_merge(fa_ObserveState(state_dict[(1, 1)]), fa_ObserveState(state_dict[(1, 2)]))  # find combined state in [lane length, lane times,lane lights]
    # cur state for each intersection west east north south
    if (flag == 0):
        n+=1
        actionindex = fa_takeAction(sigma)
        action = list_of_actiontodict[actionindex]
        if n != 1:
            UpdateQvaluefa(prev_state, sigma)
    elif flag == 1:
        n+=1
        actionindex = fa_actionoptimal(sigma)
        action = list_of_actiontodict[actionindex]

    prev_action = list_of_actiontodict[actionindex]
    prev_state = sigma
    return action