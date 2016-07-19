

#made the code scalable


import random
import math
#import network_control

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

def square_coord(i, a):
    if (i%a == 0):
        return (int(i/a), a)
    else:
        return (int(i/a)+1, i%a)


def creat_listofdict(clusters, a, list_of_actiontodict, num_inter):
    base = 1
    for key in clusters:

        list_of_actiontodict[key] = ['null']
        num_intersection = len(clusters[key])


        case = [0] * num_inter
        for iter in range(0, 2 ** num_intersection):
            d = {}
            for i in range(base, base + num_intersection):
                d[square_coord(i, a)] = case[i - 1]

            case[num_intersection - 1] += 1
            checkfor1(case, num_intersection - 1)
            list_of_actiontodict[key].append(d)

        base += num_intersection




def create_table(clusters, SATable):
    for key in clusters:
        SATable[key] = []
        num_intersection = len(clusters[key])
        i = [1]*6*num_intersection
        while (i != [3] * 6 * num_intersection):
            j = []
            for item in i:
                j.append(item)
            SATable[key].append([j] + [0] * (2 ** num_intersection))
            i[6 * num_intersection - 1] += 1
            checkfor3(i, 6 * num_intersection - 1)
        SATable[key].append([i] + [0] * (2 ** num_intersection))



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
    state = [lane_threshold(lane1), lane_threshold(lane2), lane_threshold(lane3), lane_threshold(lane4), \
             time_threshhold(time1), time_threshhold(time2)]
    return state


def findindex(state, num_intersection):

    index = 0
    for i in range(0, 6*num_intersection):
        index += (3 ** (6*num_intersection - 1 - i)) * (state[i] - 1)
    return index


def reward(state1, state2, num_intersection):
    "Started in state1 action was taken to get to state2, calculates a reward used in Q-Learning formula"
    a = 1
    b = 1
    c = 0
    sumlanelength1 = 0
    sumlanelength2 = 0
    sumtime1 = 0
    sumtime2 = 0
    while c < 6*num_intersection:
        for i in range(c, c+4):
            sumlanelength1 += state1[i]
            sumlanelength2 += state2[i]
        sumtime1 += state1[c+4]
        sumtime1 += state1[c+5]
        sumtime2 += state2[c+4]
        sumtime2 += state2[c+5]
        c += 6
    reward = a * (sumlanelength1 - sumlanelength2) + b * (sumtime1 - sumtime2)
    return reward


def UpdateQvalue(state1, state2, action, SATable, c, n, c_num):

    index1 = findindex(state1, c_num)
    index2 = findindex(state2, c_num)
    alpha = (1/float(n))
    gamma = 0.9
    SATable[c][index1][action] = round(((1 - alpha) * (SATable[c][index1][action]) + alpha * (reward(state1, state2, c_num) + \
                                  gamma * (max(SATable[c][index2][1], SATable[c][index2][2], SATable[c][index2][3], \
                                               SATable[c][index2][4])))),10)
    print(str(state1) +' '+ str(action) +' '+ str(c) +' '+ str(n))
    print(SATable[c][index1][action])


def takeAction(state1, SATable, c, c_num):
    "Decide which action to take based on optimal Q-Value with epsilon greedy algorithm"

    a = random.random()
    if a <= 0.9:
        stateindex = findindex(state1, c_num)
        indexmax = 1 #index of action with max qvalue
        indexsame = [] #list of indices with same max qvalue
        for i in range (2,2**c_num+1):
            if SATable[c][stateindex][i] > SATable[c][stateindex][indexmax]:
                indexmax = i
                indexsame = []
            if SATable[c][stateindex][i] == SATable[c][stateindex][indexmax]:
                indexsame.append(i)
        if indexsame != []: # if indexsame == [] means that indexmax is only max qvalue
            indexsame.append(indexmax)
            randomindex = random.randint(0,len(indexsame)-1)
            return indexsame[randomindex]
        else:
            return indexmax
    else:
        actionindex = random.randint(1,2**c_num)
        return actionindex

SATable = {}
n = 0
list_of_actiontodict = {1:['null', {(1, 2): 0, (1, 1): 0}, {(1, 2): 1, (1, 1): 0}, {(1, 2): 0, (1, 1): 1}, {(1, 2): 1, (1, 1): 1}], \
                        2:['null', {(1, 3): 0, (2,3): 0}, {(1, 3): 1, (2,3): 0}, {(1, 3): 0, (2,3): 1},
                         {(1, 3): 1, (2,3): 1}], \
                        3:['null', {(2, 1): 0, (2, 2): 0}, {(2, 2): 1, (2, 1): 0}, {(2, 2): 0, (2, 1): 1},
                         {(2, 2): 1, (2, 1): 1}]}
num_intersections = 0
a = 0


def init_qlearning(clusters):
    global SATable
    global n
    global list_of_actiontodict
    global num_intersections
    global a
    for key in clusters:
        for e in clusters[key]:
            num_intersections += 1
    a = int(num_intersections**0.5)+1

    #creat_listofdict(clusters, a , list_of_actiontodict, num_intersections)
    create_table(clusters, SATable)



def qlearning(state_dict, clusters,prev_state_global,cur_state_global,prev_action_global, n_global):
    global SATable
    global list_of_actiontodict


     
    init_qlearning(clusters)
    actions = {}
    
    for key in clusters:
        
        states = []
        
        for e in clusters[key]:
            states.append(ObserveState(state_dict[e]))

        n_global[key-1]+=1
        temp_states = []
        for e in states:
            temp_states += e
        cur_state_global[key-1] = temp_states
        actionindex = takeAction(cur_state_global[key-1], SATable, key, len(clusters[key]))
        action = list_of_actiontodict[key][actionindex]
        if prev_state_global[key-1] != []:
            UpdateQvalue(prev_state_global[key-1], cur_state_global[key-1], prev_action_global[key-1], SATable, key, n_global[key-1], len(clusters[key]))
        prev_state_global[key-1] = cur_state_global[key-1]
        prev_action_global[key-1] = actionindex
        for k in action:
            actions[k] = action[k]


    return actions    

