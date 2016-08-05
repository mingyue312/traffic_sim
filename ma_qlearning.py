import random
import numpy as np

k = 0 #k is a timestep counter
numofinter = 0
numofneighbours = 3
numofstates = 0
#i will have a dictionary like so: {(1,1):[1,2,3,4], (1,2):[1,2,3,4]}
agents = [(1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(3,1),(3,2),(3,3)]
adjmat = [[0,1,1,0,0,0,0,0,0],[1,0,1,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,1,0],[0,0,0,0,0,1,0,0,1],[0,0,0,0,1,0,0,0,1],[0,0,0,1,0,0,0,1,0],[0,0,0,1,0,0,1,0,0],[0,0,0,0,1,1,0,0,0]]
Mmatrices = {}
Countmatrices = {}
Qmatrices = {}

prevaction = 0
prevstate = NULL

def initialize(input_numofinter,input_numofneighbours):
    global Mmatrices
    global Qmatrices
    global numofneighbours
    global numofinter
    global agents
    global numofstates
    numofneighbours = input_numofneighbours
    numofinter = input_numofinter

    for i in range(0,numofinter):
        for j in range(0,numofinter):
            #i is the agent inter j is the neighbour inter
            if adjmat[i][j] == 1:
                Mmatrices[(agents[i],agents[j])] = np.full((numofstates, 2), 1 / 2)
                Countmatrices[(agents[i],agents[j])] = np.zeros((numofstates, 2))
                Qmatrices[(agents[i],agents[j])] = np.zeros((numofstates, 2))
    return

def findindex():


def lanethreshold(int):
    if int < 5:
        return 0
    if int < 10:
        return 0.5
    if int < 15:
        return 1

def timethreshold(int):
    if int < 5:
        return 0
    else:
        return 1

def threshold(state_list):
    state = [max(state_list[])]#ENTER CORRECT INDICES HERE AFTER ASKING MING
    reduced_state = [lanethreshold(state_list[0]),lanethreshold(state_list[1]),timethreshold(state_list[2]),timethreshold(state_list[3])]
    return reduced_state

def reward(agentstatetimek2, neighbourstatetimek2):
    global prevstate

    agentstatetimek1 = prevstate[0]
    neighbourstatetimek1 = prevstate[1]
    lane_sumtimek1 = sum(agentstatetimek1[0:2])+sum(neighbourstatetimek1[0:2])
    lane_sumtimek2 = sum(agentstatetimek2[0:2])+sum(neighbourstatetimek2[0:2])
    time_sumtimek1 = sum(agentstatetimek1[2:4])+sum(neighbourstatetimek1[2:4])
    time_sumtimek2 = sum(agentstatetimek2[2:4])+sum(neighbourstatetimek2[2:4])
    reward = (lane_sumtimek1+time_sumtimek1) - (lane_sumtimek2+time_sumtimek2)
    return reward


def observe(state_dict,agentindex,neighbourindex):
    global prevaction
    global agents

    actionindextimek1 = prevaction
    reduced_state_agenttimek2 = threshold(state_dict[agents[agentindex]])
    reduced_state_neighbourtimek2 = threshold(state_dict[agents[neighbourindex]])
    return (reduced_state_agenttimek2+reduced_state_neighbourtimek2, actionindextimek1)

def updateCount(agentindex, neighbourindex, stateindex, actionindex):
    global k
    global Countmatrices
    global agents

    k +=1
    Countmatrices[(agents[agentindex], agents[neighbourindex])][stateindex][actionindex-1] += 1
    return


def updateM(agentindex, neighbourindex, stateindex):
    global Countmatrices
    global agents


    totalcount = (Countmatrices[(agents[agentindex], agents[neighbourindex])][stateindex][0]+\
    Countmatrices[(agents[agentindex], agents[neighbourindex])][stateindex][1])
    Mmatrices[(agents[agentindex], agents[neighbourindex])][stateindex][0] = \
    Countmatrices[(agents[agentindex], agents[neighbourindex])][stateindex][0]\totalcount
    Mmatrices[(agents[agentindex], agents[neighbourindex])][stateindex][1] = \
    Countmatrices[(agents[agentindex], agents[neighbourindex])][stateindex][1]\totalcount
    return

def updateQ(agentindex, neighbourindex, stateindex, actionindex,max_expectedqvalue):
    Qmatrices[(agents[agentindex], agents[neighbourindex])][stateindex][0]



def maxexpectedqvalue(agentindex, neighbourindex, stateindex):
    global agents
    global Mmatrices
    global Qmatrices

    maxqvalue = -999999999999
    for i in range(0,maxnumofstates):
        mvaluea0 = Mmatrices[(agents[agentindex], agents[neighbourindex])][stateindex][0]
        mvaluea1 = Mmatrices[(agents[agentindex], agents[neighbourindex])][stateindex][1]
        qvaluea0 = Qmatrices[(agents[agentindex], agents[neighbourindex])][stateindex][0]
        qvaluea1 = Qmatrices[(agents[agentindex], agents[neighbourindex])][stateindex][1]
        qvalue = mvaluea0*qvalue0+mvaluea1*qvaluea1
        if qvalue >= maxqvalue:
            maxqvalue = qvalue
    return qvalue



def takeaction(agentindex, neighbourindex, stateindex):
    global agents
    global Mmatrices
    global Qmatrices

    if Qmatrices[(agents[agentindex], agents[neighbourindex])][stateindex][0] >= Qmatrices[(agents[agentindex], agents[neighbourindex])][stateindex][1]:
        if Qmatrices[(agents[agentindex], agents[neighbourindex])][stateindex][0] = Qmatrices[(agents[agentindex], agents[neighbourindex])][stateindex][1]:
            a = random.random()
            if a > 0.5:
                return 0
            else:
                return 1
        else:
            return 0
    if Qmatrices[(agents[agentindex], agents[neighbourindex])][stateindex][0] < Qmatrices[(agents[agentindex], agents[neighbourindex])][stateindex][1]:
        return 1



def Qlearning(state_dict):
    global numofinter

    dictofaction = {}
    for i in in range(0,numofinter):
        for j in range(0,numofinter):
            if adjmat[i][j] == 1:
                jointstate_and_action_tuple = observe(state_dict, i, j)
                stateindex = findindex(jointstate_and_action_tuple[0])
                actionindex = jointstate_and_action_tuple[1] #this is just the previous action
                updateCount(i, j, stateindex, actionindex)
                updateM(i, j, stateindex)
                max_expectedqvalue = maxexpectedqvalue(agentindex, neighbourindex, stateindex)
                updateQ(i, j, stateindex, actionindex,max_expectedqvalue)
                curactionindex  = takeaction(agentindex, neighbourindex, stateindex)
                prevstate = stateindex
                prevaction = curactionindex
                dictofaction[agents[agentindex]] = curaction

