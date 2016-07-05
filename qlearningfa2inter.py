import random
import numpy as np

"""
2 intersections
given a state in the simulation the agent must:
1. Observe the state and store the state information.
2. Lookup state in state action table
3. Choose the action with most optimal Q-Value 90% chance. Choose random action 10% of times (Random action can be
   taken using random number. Two possible actions in any given state: change light/don't change light.
4. After a 5 second duration observe the state and update previous state-action Q-Value.
5. Repeat steps 2 to 5 until simulation is complete. Analyze the state action table.

Notes:
    We will need a function to:
    - Observe the current state
        Input: Data stored in simulation (lane lengths and time lane has been red). Data can be stored as list
        of lists or using tuples.
        Output: list/tuple containing state ( i.e [[short,10sec], [short,10sec], ...] )
        Remarks: Since we are considering one traffic junction we can label the lanes using numbers
        (i.e lane0, lane1, ...) These will correspond to the indices in the list that is lane 0 will be
        represented by the 0th element in the list.

    - Max function
        Input: Two Numbers
        Output: Max number
        Remarks: Returns the max number between two numbers

    - Choose which action to take
        Input: State
        Output: Action
        Remarks: Needs to search through to the S-A table to find the Q-Values for the action. Note that
        there are two possible actions: change the lights, do not change the lights. Will choose action
        with highest Q-Value 90% of time, and randomly 10% of the time based on state-action table.

    - Update Q-Values
        Input:
        Output:
        Remarks:

    - Main function that continuously uses other functions to allow for Q-Learning
        Inputs:
        Outputs:
        Remarks: At the end of this function if possible print the S-A table for analysis.


    We will need:
    - A state-action table which contains all actions for every state and will store its corresponding Q-Value.
    This can be accomplished using a list of list. Can be made a global variable.
    -

Questions:
    - How will time be simulated?

Things to do:
2. for observe state function find out how to get the state array
3. make the initialization for SATable scalable
4. Find a similar way (i.e. array) to get state information from simulation for larger networks
5.


input:
{(1,1):[1,2,3,4,5,6,7,8,9], (1,2):[1,2,3,4,5,6,7,8,9]}
I want to take this and convert it into:
[1,2,3,4,5,6,7,8,9,10]

i want to return
e.g. {(1,1):1, (1,2):0}
"""
############################################################################################
# Code Begins:

# Initializing global variables
SATable = []
SATableoptimal = []
n = 0
flag = 0
prev_state = []
prev_action = -1
list_of_actiontodict = ["null",{(1,1):0, (1,2):0}, {(1,1):0, (1,2):1}, {(1,1):1, (1,2):0}, {(1,1):1, (1,2):1}]
theta = np.array( ((0),(0),(0),(0),(0),(0),(0),(0),(0),(0)) )
# Initializing the State-Action Table
# The table will be a list of lists. Each list element will contain:
# [[5 digit state ID], q-value for action 0, q-value for action 1]
# Note: action 0-> take no action; action 1-> change signal light
def checkfor3(i,n):
    if i[n] == 4:
        i[n-1] += 1
        i[n] = 1
        checkfor3(i,n-1)

i = [1, 1, 1, 1, 1,1, 1, 1, 1, 1]
while i != [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]:
    j = []
    for item in i:
        j.append(item)
    SATable.append([j,0,0,0,0])
    i[9] += 1
    checkfor3(i,9)
SATable.append([i,0,0,0,0])

#
# def initialize_list_of_actiontodict(num_of_inter):
#
#
# def initialize(num_of_inter):
#     theta = num_of_inter*[0, 0, 0, 0, 0]
#     list_of_actiontodict = initialize_list_of_actiontodict(num_of_inter)

######################
# #Helper Functions:

def lane_threshold(a):
    "convert car length in a lane into thresholds 1-short 2-intermediate 3-long"
    if a <= 5:
        return 1
    elif (a > 5 and a < 12):
        return 2
    elif (a >= 12):
        return 3


def time_threshhold(a):
    "convert time signal has been red into thresholds 1-short 2-intermediate 3-long"
    if a <= 4:
        return 1
    elif (a > 4 and a <= 8):
        return 2
    elif (a > 8):
        return 3


def ObserveState(state_array):
    "Given a state array - [number of cars in westr, westl, ..., eastl, eastr, red time] return the state ID"

    lane1 = max(state_array[0], state_array[1])
    lane2 = max(state_array[2], state_array[3])
    lane3 = max(state_array[4], state_array[5])
    lane4 = max(state_array[6], state_array[7])
    time = state_array[8]
    state = [lane_threshold(lane1), lane_threshold(lane2), lane_threshold(lane3), lane_threshold(lane4), \
             time_threshhold(time)]
    return state

def merge(state1, state2):
    #sigma = state
    sigma = state1[0:4]+state2[0:4]+state1[4]+state2[4]
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

def cost(state1):
    a = 1
    b = 1
    c = 0
    sumlanelength1 = 0
    sumtime1 = 0
    while c < 9:
        for i in range(c, c + 4):  # 0,1,2,3 (0-4), 5,6,7,8 (5-9)
            sumlanelength1 += state1[i]
        sumtime1 += state1[c + 4]
        c += 5
    cost = a*(sumlanelength1) + b*(sumtime1)
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
    global SATable
    global theta
    global n
    global flag
    #cur_state is equal to sigma in the literture
    alpha = 1/(float(n))
    gamma = 0.9
    cost = cost(ps)
    sigma = np.array( ((ps[0]),(ps[1]),(ps[2]),(ps[3]),(ps[4]),(ps[5]),(ps[6]),(ps[7]),(ps[8]),(ps[9])) )
    theta += alpha*sigma*( cost + gamma*() )



def takeAction(state1):
    "Decide which action to take based on optimal Q-Value with epsilon greedy algorithm"
    global SATable
    global list_of_actiontodict
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
    if (flag == 0):
        cur_state = merge(ObserveState(state_dict[(1, 1)]), ObserveState(state_dict[(1, 2)])) # find combined state id
        n+=1
        actionindex = takeAction(cur_state)
        action = list_of_actiontodict(actionindex)
        if n != 1:
            UpdateQvaluefa(prev_state, cur_state)