

#made the code scalable


import random
import math
from collections import OrderedDict

SATable = []
n = 0
prev_state = []
prev_action = -1
num_intersection = 2
a = int(num_intersection**(1/2))

#list_of_actiontodict = ["null",{(1,1):0, (1,2):0}, {(1,1):0, (1,2):1}, {(1,1):1, (1,2):0}, {(1,1):1, (1,2):1}]
list_of_actiontodict = ["null"]

def checkfor1(i,n):
    if i[n] == 2:
        i[n - 1] += 1
        i[n] = 0
        checkfor1(i, n - 1)

def checkfor3(i,n):
    if i[n] == 4:
        i[n-1] += 1
        i[n] = 1
        checkfor3(i,n-1)

def square_coord(i):
    if (i%a == 0):
        return (int(i/a), a)
    else:
        return (int(i/a)+1, i%a)


def creat_listofdict():
    global list_of_actiontodict

    case = [0]*num_intersection

    for iter in range (0, 2**num_intersection):
        d = {}
        for i in range (1,num_intersection+1):

            d[square_coord(i)] = case[i-1]

        case[num_intersection - 1] += 1
        checkfor1(case, num_intersection - 1)
        OrderedDict(sorted(d.items()))
        list_of_actiontodict.append(d)









def create_table():
    global SATable
    global num_intersection

    i = [1]*4*num_intersection

    while (i != [3]*4*num_intersection):
        j = []
        for item in i:
            j.append(item)
        SATable.append([j]+[0]*(2**num_intersection))
        i[4*num_intersection-1] += 1
        checkfor3(i, 4*num_intersection-1)
    SATable.append([i]+[0]*(2**num_intersection))



######################
# #Helper Functions:

def lane_threshold(a):
    "convert car length in a lane into thresholds 1-short 2-intermediate 3-long"
    if a <= 6:
        return 1
    elif (a > 6 and a < 16):
        return 2
    elif (a >= 16):
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
    time1 = state_array[8]
    time2 = state_array[9]
    state = [lane_threshold(lane1) + lane_threshold(lane3), lane_threshold(lane2) + lane_threshold(lane4), \
             time_threshhold(time1), time_threshhold(time2)]
    return state


def findindex(state):
    "Given the state ID returns state index in the SATable"
    global num_intersection
    index = 0
    for i in range(0, 4*num_intersection):
        index += (3 ** (4*num_intersection - 1 - i)) * (state[i] - 1)
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
    while c < 4*num_intersection:
        for i in range(c, c+2): #0,1,2,3 (0-4), 5,6,7,8 (5-9)
            sumlanelength1 += state1[i]
            sumlanelength2 += state2[i]
        sumtime1 += state1[c+2]
        sumtime1 += state1[c+3]
        sumtime2 += state2[c+2]
        sumtime2 += state2[c+3]
        c += 4
    reward = a * (sumlanelength1 - sumlanelength2) + b * (sumtime1 - sumtime2)
    return reward


def UpdateQvalue(state1, state2, action):
    global SATable
    global n
    index1 = findindex(state1)
    index2 = findindex(state2)
    alpha = (1/float(n))
    gamma = 0.9
    localoldqvalue = SATable[index1][action]
    SATable[index1][action] = round(((1 - alpha) * (SATable[index1][action]) + alpha * (reward(state1, state2) + \
                                  gamma * (max(SATable[index2][1], SATable[index2][2], SATable[index2][3], SATable[index2][4])))),10)



def takeAction(state1):
    "Decide which action to take based on optimal Q-Value with epsilon greedy algorithm"
    global SATable
    global list_of_actiontodict
    a = random.random()
    if a <= 0.65:
        stateindex = findindex(state1)
        indexmax = 1 #index of action with max qvalue
        indexsame = [] #list of indices with same max qvalue
        for i in range (2,2**num_intersection+1):
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
        actionindex = random.randint(1,2**num_intersection)
        return actionindex


def qlearning(state_dict):
    global prev_state
    global prev_action
    global n
    create_table()
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


create_table()
print(len(SATable))
print(3**8)
print(SATable)

print(SATable[162])
print(findindex([1, 1, 1, 3, 1, 1, 1, 1]))



creat_listofdict()
print(len(list_of_actiontodict))
print(list_of_actiontodict)

print(reward([1]*8,[2]*8))