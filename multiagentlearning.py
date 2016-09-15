import random
import numpy as np

'''
things to do:
rewrite adj matrix
'''
k = 1 #k is a timestep counter
numofinter = 25

numofneighbours = 4
numofstates = 1296
#i will have a dictionary like so: {(1,1):[1,2,3,4], (1,2):[1,2,3,4]}
agents = [(1,1),(1,2),(1,3),(1,4),(1,5),(2,1),(2,2),(2,3),(2,4),(2,5),(3,1),(3,2),(3,3),(3,4),(3,5),(4,1),(4,2),(4,3),(4,4),(4,5),(5,1),(5,2),(5,3),(5,4),(5,5)]
adjmat = \
[
    [0,1,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
    [1,0,1,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
    [0,1,0,1,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
    [0,0,1,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
    [0,0,0,0,0, 0,0,0,0,1, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
    [0,0,0,0,0, 0,0,0,0,0, 1,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
    [0,0,0,0,0, 0,0,1,0,0, 0,1,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
    [0,0,0,0,0, 0,1,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
    [0,0,0,0,0, 0,0,0,0,0, 0,0,0,1,0, 0,0,0,0,0, 0,0,0,0,0],
    [0,0,0,0,1, 0,0,0,0,0, 0,0,0,0,1, 0,0,0,0,0, 0,0,0,0,0],
    [0,0,0,0,0, 1,0,0,0,0, 0,0,0,0,0, 1,0,0,0,0, 0,0,0,0,0],
    [0,0,0,0,0, 0,1,0,0,0, 0,0,0,0,0, 0,1,0,0,0, 0,0,0,0,0],
    [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
    [0,0,0,0,0, 0,0,0,1,0, 0,0,0,0,0, 0,0,0,1,0, 0,0,0,0,0],
    [0,0,0,0,0, 0,0,0,0,1, 0,0,0,0,0, 0,0,0,0,1, 0,0,0,0,0],
    [0,0,0,0,0, 0,0,0,0,0, 1,0,0,0,0, 0,0,0,0,0, 1,0,0,0,0],
    [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,1,0,0,0, 0,0,0,0,0],
    [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,1,0, 0,0,0,0,0],
    [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,1,0,0, 0,0,0,0,0],
    [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,1, 0,0,0,0,0, 0,0,0,0,0],
    [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 1,0,0,0,0, 0,0,0,0,0],
    [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,1,0,0],
    [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,1,0,1,0],
    [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,1,0,1],
    [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,1,0],
]
Mmatrices = {}
Countmatrices = {}
Qmatrices = {}

prevaction = {(1,1):1,(1,2):1,(1,3):1,(1,4):1,(1,5):1,(2,1):1,(2,2):1,(2,3):1,(2,4):1,(2,5):1,(3,1):1,(3,2):1,(3,3):1,(3,4):1,(3,5):1,(4,1):1,(4,2):1,(4,3):1,(4,4):1,(4,5):1,(5,1):1,(5,2):1,(5,3):1,(5,4):1,(5,5):1}
prevstate = {(1,1):[0,0,0,0],(1,2):[0,0,0,0],(1,3):[0,0,0,0],(1,4):[0,0,0,0],(1,5):[0,0,0,0],(2,1):[0,0,0,0],(2,2):[0,0,0,0],(2,3):[0,0,0,0],(2,4):[0,0,0,0],(2,5):[0,0,0,0],(3,1):[0,0,0,0],(3,2):[0,0,0,0],(3,3):[0,0,0,0],(3,4):[0,0,0,0],(3,5):[0,0,0,0],(4,1):[0,0,0,0],(4,2):[0,0,0,0],(4,3):[0,0,0,0],(4,4):[0,0,0,0],(4,5):[0,0,0,0],(5,1):[0,0,0,0],(5,2):[0,0,0,0],(5,3):[0,0,0,0],(5,4):[0,0,0,0],(5,5):[0,0,0,0]}

def initialize(input_numofinter,input_numofneighbours):
    global Mmatrices
    global Qmatrices
    global numofneighbours
    global numofinter
    global agents
    global numofstates
    # numofneighbours = input_numofneighbours
    # numofinter = input_numofinter

    for i in range(0,numofinter):
        agentneighbourexists = 0
        for j in range(0,numofinter):
            #i is the agent inter j is the neighbour inter
            if adjmat[i][j] == 1:
                agentneighbourexists = 1
                Mmatrices[(agents[i],agents[j])] = np.full((numofstates, 2), 1 / 2)
                Countmatrices[(agents[i],agents[j])] = np.zeros((numofstates, 2))
                Qmatrices[(agents[i],agents[j])] = np.zeros((numofstates, 4))
        if agentneighbourexists == 0:
            Qmatrices[(agents[i],agents[i])] = np.zeros((numofstates, 4))
    return

def findindex(jointstate):
    index = jointstate[7] + jointstate[6]*2 + jointstate[5]*4 + jointstate[4]*8 + jointstate[3]*32 + jointstate[2]*32*3 + jointstate[1]*32*9 + jointstate[0]*32*27
    index = int(index)
    return index

def findactionindex(actiontuple):
    '''
    takes in an agent neighbour action pair and returns index
    this is useful for accessing elements in the Q-matrix
    actionpairs: (0,0),(0,1),(1,0),(1,1)
    actionindex:  0,     1,    2,    3
    '''
    index = 0
    if actiontuple[1] == 1:
        index += 1
    if actiontuple[0] == 1:
        index += 2
    return index

def lanethreshold(int):
    if int < 4:
        return 0
    elif int < 8:
        return 0.5
    else:
        return 1

def timethreshold(int):
    if int < 10:
        return 0
    else:
        return 1

def threshold(state_list):
    state = [max(state_list[0:4]), max(state_list[4:8]),state_list[8], state_list[9]]
    reduced_state = [lanethreshold(state[0]),lanethreshold(state[1]),timethreshold(state[2]),timethreshold(state[3])]
    return reduced_state

def calcreward(agentstatetimek1, neighbourstatetimek1, agentstatetimek2, neighbourstatetimek2):
    '''c
    calculates reward based on difference between two states
    '''


    lane_sumtimek1 = sum(agentstatetimek1[0:2])+sum(neighbourstatetimek1[0:2])
    lane_sumtimek2 = sum(agentstatetimek2[0:2])+sum(neighbourstatetimek2[0:2])
    time_sumtimek1 = sum(agentstatetimek1[2:4])+sum(neighbourstatetimek1[2:4])
    time_sumtimek2 = sum(agentstatetimek2[2:4])+sum(neighbourstatetimek2[2:4])
    reward = (lane_sumtimek1+time_sumtimek1) - (lane_sumtimek2+time_sumtimek2)
    return reward


def observe(state_dict,agentindex,neighbourindex):
    #a - agent, n-neighbour, l-lane, h-horizontal, v-vertical, c-count, t-time
    #returns ([ahlc, avlc, ahlt, avlt, nhlc, nvlc, nhlt, nvlt], actiontuple)

    global prevaction
    global agents

    actiontupletimek1 = (prevaction[agents[agentindex]], prevaction[agents[neighbourindex]])
    reduced_state_agent_time_k2 = threshold(state_dict[agents[agentindex]])
    reduced_state_neighbourtimek2 = threshold(state_dict[agents[neighbourindex]])
    return (reduced_state_agent_time_k2+reduced_state_neighbourtimek2, actiontupletimek1)

def updateCount(agentindex, neighbourindex, prevstateindex, neighactionindex):
    global k
    global Countmatrices
    global agents

    Countmatrices[(agents[agentindex], agents[neighbourindex])][prevstateindex][neighactionindex] += 1
    return


def updateM(agentindex, neighbourindex, stateindex):
    '''
    updates the M-matrix
    '''
    global Countmatrices
    global agents


    totalcount = (Countmatrices[(agents[agentindex], agents[neighbourindex])][stateindex][0]+\
    Countmatrices[(agents[agentindex], agents[neighbourindex])][stateindex][1])
    Mmatrices[(agents[agentindex], agents[neighbourindex])][stateindex][0] = \
    Countmatrices[(agents[agentindex], agents[neighbourindex])][stateindex][0]/totalcount
    Mmatrices[(agents[agentindex], agents[neighbourindex])][stateindex][1] = \
    Countmatrices[(agents[agentindex], agents[neighbourindex])][stateindex][1]/totalcount
    return

def updateQ(agentindex, neighbourindex, stateindex, actiontuple,max_expectedqvalue,reward):
    global k

    alpha = 1/float(k)
    gamma = 0.9
    actionindex = findactionindex(actiontuple) #this is the column of the qvalue to be updated
    oldq = Qmatrices[(agents[agentindex], agents[neighbourindex])][stateindex][actionindex]
    Qmatrices[(agents[agentindex], agents[neighbourindex])][stateindex][actionindex] = (1-alpha)*oldq+alpha*(reward+gamma*max_expectedqvalue)
    return



def maxexpectedqvalue(agentindex, neighbourindex, curstateindex):
    global agents
    global Mmatrices
    global Qmatrices

    maxqvalue = -999999999999
    for agentaction in range(0,2):
        qvalue = 0
        for neighbouraction in range(0,2):
            qvalue += Qmatrices[(agents[agentindex], agents[neighbourindex])][curstateindex][findactionindex((agentaction,neighbouraction))]* \
                     Mmatrices[(agents[agentindex], agents[neighbourindex])][curstateindex][neighbouraction]
        if qvalue >= maxqvalue:
            maxqvalue = qvalue

    return qvalue



def takeaction(agentindex, neighbourindex, stateindex):
    global agents
    global Mmatrices
    global Qmatrices

    if Qmatrices[(agents[agentindex], agents[neighbourindex])][stateindex][0] >= Qmatrices[(agents[agentindex], agents[neighbourindex])][stateindex][1]:
        if Qmatrices[(agents[agentindex], agents[neighbourindex])][stateindex][0] == Qmatrices[(agents[agentindex], agents[neighbourindex])][stateindex][1]:
            return random.randint(0,1)
        else:
            return 0
    if Qmatrices[(agents[agentindex], agents[neighbourindex])][stateindex][0] < Qmatrices[(agents[agentindex], agents[neighbourindex])][stateindex][1]:
        return 1



def qlearning(state_dict):
    global numofinter
    global prevaction
    global prevstate
    global agents
    global k
    global Qmatrices

    action_dict = {}
    for i in range(0,numofinter):
        agentindex = i
        agentneighbourexists = 0 #this is a flag variable
        for j in range(0,numofinter):
            if adjmat[i][j] == 1:
                agentneighbourexists =1
                neighbourindex = j
                #store the jointstate of the agent and neighbour, and the prev actions
                #stored as: ([jointstate list], (agent_prev_action, neighbour_prev_action))
                jointstate_and_action_tuple = observe(state_dict, i, j)
                # find the index of the jointstate to help access elements in M/Q matrix
                stateindex = findindex(jointstate_and_action_tuple[0])
                #update count matrix and M matrix
                neighactionindex = jointstate_and_action_tuple[1][1]
                updateCount(i, j, stateindex, neighactionindex)
                updateM(i, j, stateindex)
                #compute the maximum expected qvalue
                max_expectedqvalue = maxexpectedqvalue(agentindex, neighbourindex, stateindex)
                #compute the reward based on previous state
                reward = calcreward(prevstate[agents[agentindex]], prevstate[agents[neighbourindex]], jointstate_and_action_tuple[0][0:4],jointstate_and_action_tuple[0][4:8])
                #update qvalue for agent-naighbour q matrix[row:prev_jointstate][column: prev_actiontuple]
                #*********************************************************************************************
                # double check this i think we may be passing current jointstate although we need prevjointstate
                # also double check findindex function
                #*********************************************************************************************
                # below updating qfunction uses stateindex of prev state of agent
                prevjointstate = prevstate[agents[agentindex]]+prevstate[agents[neighbourindex]]
                updateQ(i, j, findindex(prevjointstate), jointstate_and_action_tuple[1],max_expectedqvalue,reward)
        if agentneighbourexists == 0:
            state_and_action_tuple = observe(state_dict,i,i)
            stateindex = findindex(state_and_action_tuple[0])
            prevagentstate = prevstate[agents[agentindex]]+prevstate[agents[agentindex]]
            max_expectedqvalue = max(Qmatrices[(agents[agentindex],agents[agentindex])][stateindex])
            reward = calcreward(prevstate[agents[agentindex]],prevstate[agents[agentindex]],state_and_action_tuple[0][0:4],state_and_action_tuple[0][4:8])
            updateQ(agentindex,agentindex,findindex(prevagentstate),state_and_action_tuple[1],max_expectedqvalue,reward/2)


        #Take action
        if k <= 2000:
            if agentneighbourexists == 0:
                epsilon = random.random()
                if epsilon < 0.6:
                    if Qmatrices[(agents[agentindex],agents[agentindex])][stateindex][0] == Qmatrices[(agents[agentindex],agents[agentindex])][stateindex][3]:
                        randomnum = random.random()
                        if randomnum < 0.5:
                            curaction = 0
                        else:
                            curaction = 1
                    elif Qmatrices[(agents[agentindex],agents[agentindex])][stateindex][0] > Qmatrices[(agents[agentindex],agents[agentindex])][stateindex][3]:
                        curaction = 0
                    else:
                        curaction = 1
                else:
                    randomnum = random.random()
                    if randomnum < 0.5:
                        curaction = 0
                    else:
                        curaction = 1


            else:
                epsilon = random.random()
                if epsilon < 0.6:
                    maxvalue = -9999999
                    for agentaction in range(0,2):
                        curaction = -1
                        curvalue = 0
                        for j in range(0,numofinter):
                            if adjmat[i][j] == 1:
                                neighbourindex = j
                                jointstate_and_action_tuple = observe(state_dict, i, j)
                                stateindex = findindex(jointstate_and_action_tuple[0])
                                for neighbaction in range(0,2):
                                    actiontuple = (agentaction,neighbaction)
                                    actionindex = findactionindex(actiontuple)
                                    curvalue+= (Qmatrices[(agents[agentindex], agents[neighbourindex])][stateindex][actionindex])* \
                                    (Mmatrices[(agents[agentindex], agents[neighbourindex])][stateindex][neighbaction])
                        if curvalue >= maxvalue:
                            if curvalue == maxvalue:
                                if curaction == -1:
                                    curaction = agentaction
                                else:
                                    curaction = random.randint(0,1)
                            else:
                                curaction = agentaction
                            maxvalue = curvalue
                else:
                    curaction = random.randint(0,1)

                action_dict[agents[i]] = curaction
                prevaction[agents[i]] = curaction
                prevstate[agents[i]] = jointstate_and_action_tuple[0][0:4]
        else:
            if agentneighbourexists == 0:
                if Qmatrices[(agents[agentindex], agents[agentindex])][stateindex][0] == \
                        Qmatrices[(agents[agentindex], agents[agentindex])][stateindex][3]:
                    randomnum = random.random()
                    if randomnum < 0.5:
                        curaction = 0
                    else:
                        curaction = 1
                elif Qmatrices[(agents[agentindex], agents[agentindex])][stateindex][0] > \
                        Qmatrices[(agents[agentindex], agents[agentindex])][stateindex][3]:
                    curaction = 0
                else:
                    curaction = 1

            else:
                maxvalue = -9999999
                for agentaction in range(0, 2):
                    curaction = -1
                    curvalue = 0
                    for j in range(0, numofinter):
                        if adjmat[i][j] == 1:
                            neighbourindex = j
                            jointstate_and_action_tuple = observe(state_dict, i, j)
                            stateindex = findindex(jointstate_and_action_tuple[0])
                            for neighbaction in range(0, 2):
                                actiontuple = (agentaction, neighbaction)
                                actionindex = findactionindex(actiontuple)
                                curvalue += (Qmatrices[(agents[agentindex], agents[neighbourindex])][stateindex][
                                                 actionindex]) * \
                                            (Mmatrices[(agents[agentindex], agents[neighbourindex])][stateindex][
                                                 neighbaction])
                    if curvalue >= maxvalue:
                        if curvalue == maxvalue:
                            if curaction == -1:
                                curaction = agentaction
                            else:
                                curaction = random.randint(0, 1)
                        else:
                            curaction = agentaction
                        maxvalue = curvalue

                action_dict[agents[i]] = curaction
                prevaction[agents[i]] = curaction
                prevstate[agents[i]] = jointstate_and_action_tuple[0][0:4]
    k += 1
    return action_dict

