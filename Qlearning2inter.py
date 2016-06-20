import random

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
# SATableoptimal = [[[1, 1, 1, 1, 1], -0.9969776434, -0.996939174], [[1, 1, 1, 1, 2], -0.1999492891, -0.0084639098], [[1, 1, 1, 1, 3], 0.0, 0.2857142857], [[1, 1, 1, 2, 1], -0.1509825301, -0.1510915091], [[1, 1, 1, 2, 2], -0.0012911807, 0.0258542997], [[1, 1, 1, 2, 3], 0, 0], [[1, 1, 1, 3, 1], -0.0182089756, -0.0178422974], [[1, 1, 1, 3, 2], -0.0001899966, 0.0178323591], [[1, 1, 1, 3, 3], 0, 0], [[1, 1, 2, 1, 1], -0.0242427298, -0.0240957922], [[1, 1, 2, 1, 2], -0.0606060606, 0.004700918], [[1, 1, 2, 1, 3], 0, 0], [[1, 1, 2, 2, 1], -0.035028216, 0.1233329022], [[1, 1, 2, 2, 2], -0.0185524753, 0.3307628834], [[1, 1, 2, 2, 3], -0.0002168335, 0.0908212477], [[1, 1, 2, 3, 1], -0.0518015688, 0.113753182], [[1, 1, 2, 3, 2], -0.0022794703, 0.0397472853], [[1, 1, 2, 3, 3], -0.0065977935, 0.0108240667], [[1, 1, 3, 1, 1], -0.041517319, -0.0415783101], [[1, 1, 3, 1, 2], -0.0001440247, 0.0012458128], [[1, 1, 3, 1, 3], 0, 0], [[1, 1, 3, 2, 1], -0.0096315541, 0.0829489789], [[1, 1, 3, 2, 2], -0.0006984607, 0.0887691928], [[1, 1, 3, 2, 3], 0, 0.0059780455], [[1, 1, 3, 3, 1], -0.0032865933, 0.1576140487], [[1, 1, 3, 3, 2], -0.0239462602, 0.0330998853], [[1, 1, 3, 3, 3], 3.05279e-05, 0.1734864152], [[1, 2, 1, 1, 1], -0.1873459708, -0.1876399413], [[1, 2, 1, 1, 2], 0.0309364454, -0.0016763542], [[1, 2, 1, 1, 3], 0, 0], [[1, 2, 1, 2, 1], -0.0130983633, -0.0067463112], [[1, 2, 1, 2, 2], -0.0001862024, 0], [[1, 2, 1, 2, 3], 0, 0], [[1, 2, 1, 3, 1], 0.0011592756, 0.0067383165], [[1, 2, 1, 3, 2], 0, 0.0], [[1, 2, 1, 3, 3], 0, 0], [[1, 2, 2, 1, 1], -0.0053014844, 0.0033631003], [[1, 2, 2, 1, 2], 0, 0], [[1, 2, 2, 1, 3], 0, 0], [[1, 2, 2, 2, 1], -0.0082760242, 0.013354989], [[1, 2, 2, 2, 2], 0, 0.0016621189], [[1, 2, 2, 2, 3], 0, 0.0002842962], [[1, 2, 2, 3, 1], 0.0026049911, 0.000618688], [[1, 2, 2, 3, 2], -0.0001766489, 0], [[1, 2, 2, 3, 3], 0, 0], [[1, 2, 3, 1, 1], 0.0065794014, -0.0007897075], [[1, 2, 3, 1, 2], 0, 0.0002603071], [[1, 2, 3, 1, 3], 0, 0], [[1, 2, 3, 2, 1], 0.0003184206, 0.0072336444], [[1, 2, 3, 2, 2], -0.0001365524, 0], [[1, 2, 3, 2, 3], 0, 0], [[1, 2, 3, 3, 1], 0.0060881889, 0.0019052468], [[1, 2, 3, 3, 2], 0, 0.0003516079], [[1, 2, 3, 3, 3], 0, 0.0002690908], [[1, 3, 1, 1, 1], 0.045136749, -0.017957485], [[1, 3, 1, 1, 2], 0.0027395808, 0], [[1, 3, 1, 1, 3], 0, 0], [[1, 3, 1, 2, 1], 0.0171930391, 0.0003221516], [[1, 3, 1, 2, 2], 0, 0.0005064644], [[1, 3, 1, 2, 3], 0, 0], [[1, 3, 1, 3, 1], 0.0295942579, 0.001306063], [[1, 3, 1, 3, 2], 0, 0], [[1, 3, 1, 3, 3], 0, 0], [[1, 3, 2, 1, 1], 0.0012841118, 0.0053089704], [[1, 3, 2, 1, 2], 0, 0], [[1, 3, 2, 1, 3], 0, 0], [[1, 3, 2, 2, 1], 1.03154e-05, 0.0462398201], [[1, 3, 2, 2, 2], 0, 0.0385013983], [[1, 3, 2, 2, 3], 0, 0], [[1, 3, 2, 3, 1], 0.0001980643, 0.0042847217], [[1, 3, 2, 3, 2], 0, 0], [[1, 3, 2, 3, 3], 0, 0], [[1, 3, 3, 1, 1], 0.0012310243, 0.0124506301], [[1, 3, 3, 1, 2], 0.0001134167, 0], [[1, 3, 3, 1, 3], 0, 0], [[1, 3, 3, 2, 1], 0.0050966246, 0.0013731243], [[1, 3, 3, 2, 2], 0.0003661931, 0], [[1, 3, 3, 2, 3], 0, 0], [[1, 3, 3, 3, 1], 0.0010434385, 0.0290119531], [[1, 3, 3, 3, 2], 0, 0.0002517657], [[1, 3, 3, 3, 3], 0, 0], [[2, 1, 1, 1, 1], -0.1199453513, -0.1199778612], [[2, 1, 1, 1, 2], 0.0245076956, -0.0020419473], [[2, 1, 1, 1, 3], 0.00128355, 0], [[2, 1, 1, 2, 1], -0.0043057866, -0.0044072087], [[2, 1, 1, 2, 2], 0.0002479725, -0.0006177924], [[2, 1, 1, 2, 3], 0, 0], [[2, 1, 1, 3, 1], 0.0048235338, 0.0001098176], [[2, 1, 1, 3, 2], 0, 0.0001967786], [[2, 1, 1, 3, 3], 0, 0], [[2, 1, 2, 1, 1], 0.0032705146, -0.0181707743], [[2, 1, 2, 1, 2], -0.0003710553, 0], [[2, 1, 2, 1, 3], 0, 0], [[2, 1, 2, 2, 1], 0, 0.0050333221], [[2, 1, 2, 2, 2], 0, 0.0010118696], [[2, 1, 2, 2, 3], 0, 0], [[2, 1, 2, 3, 1], -0.0005882466, 0.0013635324], [[2, 1, 2, 3, 2], 0, 0], [[2, 1, 2, 3, 3], 0, 0], [[2, 1, 3, 1, 1], -0.0005938242, 0.0066683332], [[2, 1, 3, 1, 2], 0, 0], [[2, 1, 3, 1, 3], 0, 0], [[2, 1, 3, 2, 1], 0.0029010715, 0.0002750858], [[2, 1, 3, 2, 2], -0.0001717811, 0], [[2, 1, 3, 2, 3], 0, 0], [[2, 1, 3, 3, 1], 0.0028180009, 0.0009055483], [[2, 1, 3, 3, 2], 0, 0], [[2, 1, 3, 3, 3], 0, 0], [[2, 2, 1, 1, 1], 0.0695352, -0.0207917647], [[2, 2, 1, 1, 2], 0.3643024051, -0.1176629329], [[2, 2, 1, 1, 3], 0.0188641276, -0.0910565838], [[2, 2, 1, 2, 1], 0.0334595932, 0.0001034963], [[2, 2, 1, 2, 2], 0.0013455383, -0.0001931986], [[2, 2, 1, 2, 3], 0, 0.0], [[2, 2, 1, 3, 1], 0.0051523358, 0], [[2, 2, 1, 3, 2], 0.0004397669, -0.0012009642], [[2, 2, 1, 3, 3], 0, 0.0012373138], [[2, 2, 2, 1, 1], 0.0059493055, 8.76538e-05], [[2, 2, 2, 1, 2], 0.0010675382, 0], [[2, 2, 2, 1, 3], 0, 0], [[2, 2, 2, 2, 1], 0, 0], [[2, 2, 2, 2, 2], 0, 0], [[2, 2, 2, 2, 3], 0, 0], [[2, 2, 2, 3, 1], 0, 0], [[2, 2, 2, 3, 2], 0, 0], [[2, 2, 2, 3, 3], 0, 0], [[2, 2, 3, 1, 1], 0.0010577876, 0.0013468485], [[2, 2, 3, 1, 2], 0, 0], [[2, 2, 3, 1, 3], 0, 0], [[2, 2, 3, 2, 1], 9.27338e-05, 0], [[2, 2, 3, 2, 2], 0, 0], [[2, 2, 3, 2, 3], 0, 0], [[2, 2, 3, 3, 1], 0, 0.000739287], [[2, 2, 3, 3, 2], 0, 0], [[2, 2, 3, 3, 3], 0, 0], [[2, 3, 1, 1, 1], 0.1478969865, -0.0029718387], [[2, 3, 1, 1, 2], 0.0194027082, -0.0053823003], [[2, 3, 1, 1, 3], 0.0395000018, 0], [[2, 3, 1, 2, 1], 0, 0.0019893749], [[2, 3, 1, 2, 2], 0, -0.0001460772], [[2, 3, 1, 2, 3], 0, 0], [[2, 3, 1, 3, 1], 0.0083326169, -0.0006602081], [[2, 3, 1, 3, 2], 0.0006432943, -0.0013289037], [[2, 3, 1, 3, 3], 0, 0], [[2, 3, 2, 1, 1], 0.0036103959, 2.567e-07], [[2, 3, 2, 1, 2], 0, 0], [[2, 3, 2, 1, 3], 0, 0], [[2, 3, 2, 2, 1], 0.0003295381, 0], [[2, 3, 2, 2, 2], 0, 0], [[2, 3, 2, 2, 3], 0, 0], [[2, 3, 2, 3, 1], 0, 0], [[2, 3, 2, 3, 2], 0, 0], [[2, 3, 2, 3, 3], 0, 0], [[2, 3, 3, 1, 1], 9.75619e-05, 0.0030577487], [[2, 3, 3, 1, 2], 0.0003412649, 0], [[2, 3, 3, 1, 3], 0, 0], [[2, 3, 3, 2, 1], 0, 0], [[2, 3, 3, 2, 2], 0, 0], [[2, 3, 3, 2, 3], 0, 0], [[2, 3, 3, 3, 1], 0, 0.000350192], [[2, 3, 3, 3, 2], 0, 0], [[2, 3, 3, 3, 3], 0, 0], [[3, 1, 1, 1, 1], -0.0180665466, -0.0186108168], [[3, 1, 1, 1, 2], 0.0030982905, -0.002258611], [[3, 1, 1, 1, 3], 0, 0], [[3, 1, 1, 2, 1], 0.0008166611, 0.0028724267], [[3, 1, 1, 2, 2], 0, 0], [[3, 1, 1, 2, 3], 0, 0], [[3, 1, 1, 3, 1], 0.0001298622, 0.0080106431], [[3, 1, 1, 3, 2], 0, 9.58664e-05], [[3, 1, 1, 3, 3], 0, 0], [[3, 1, 2, 1, 1], 0.0004212376, -6.79355e-05], [[3, 1, 2, 1, 2], 0, 0.0001927119], [[3, 1, 2, 1, 3], 0, 0], [[3, 1, 2, 2, 1], 0, 0.0019594165], [[3, 1, 2, 2, 2], 0, 0], [[3, 1, 2, 2, 3], 0, 0], [[3, 1, 2, 3, 1], 0.0001106924, 0.0013913076], [[3, 1, 2, 3, 2], -0.0001984915, 0], [[3, 1, 2, 3, 3], 0, 0], [[3, 1, 3, 1, 1], 0.0094604618, 0.0007337371], [[3, 1, 3, 1, 2], 0, 0], [[3, 1, 3, 1, 3], 0, 0], [[3, 1, 3, 2, 1], 0.0002275449, 0.0026178468], [[3, 1, 3, 2, 2], 0.0002730575, 0], [[3, 1, 3, 2, 3], 0, 0], [[3, 1, 3, 3, 1], 0.0099677659, 0.0008235494], [[3, 1, 3, 3, 2], 0, 0], [[3, 1, 3, 3, 3], 0.0, 0.0005939577], [[3, 2, 1, 1, 1], 0.0571146541, -0.0059204608], [[3, 2, 1, 1, 2], 0.0467222945, -0.0012264851], [[3, 2, 1, 1, 3], 0.4019178204, 0], [[3, 2, 1, 2, 1], 0.0062024845, 0.0004634145], [[3, 2, 1, 2, 2], 0, 5.39438e-05], [[3, 2, 1, 2, 3], 0.0006205676, 0], [[3, 2, 1, 3, 1], 0.0060769641, 0.0004448345], [[3, 2, 1, 3, 2], 0, 0], [[3, 2, 1, 3, 3], 0, 0], [[3, 2, 2, 1, 1], 0.0003493981, -0.0018975332], [[3, 2, 2, 1, 2], 0.0057018743, 0], [[3, 2, 2, 1, 3], 0, 0], [[3, 2, 2, 2, 1], 0, 0], [[3, 2, 2, 2, 2], 0, 0], [[3, 2, 2, 2, 3], 0, 0], [[3, 2, 2, 3, 1], 0, 0], [[3, 2, 2, 3, 2], 0, 0], [[3, 2, 2, 3, 3], 0, 0], [[3, 2, 3, 1, 1], 0.0012623339, 0.0], [[3, 2, 3, 1, 2], 0, 0.0002233462], [[3, 2, 3, 1, 3], 0.0016959357, 0], [[3, 2, 3, 2, 1], 0.0007825754, 0], [[3, 2, 3, 2, 2], 0, 0], [[3, 2, 3, 2, 3], 0, 0], [[3, 2, 3, 3, 1], 0, 0], [[3, 2, 3, 3, 2], 0, 0], [[3, 2, 3, 3, 3], 0, 0], [[3, 3, 1, 1, 1], 0.1878259261, -0.0204498484], [[3, 3, 1, 1, 2], 0.0330186815, -0.0161275248], [[3, 3, 1, 1, 3], 0.0915770059, 0], [[3, 3, 1, 2, 1], 0.0186954007, 0.001769716], [[3, 3, 1, 2, 2], 0, 0], [[3, 3, 1, 2, 3], 0.0090344137, 0], [[3, 3, 1, 3, 1], 0.0007354655, 0.022211766], [[3, 3, 1, 3, 2], 0.0004164282, 0], [[3, 3, 1, 3, 3], 0.003997482, 0], [[3, 3, 2, 1, 1], 0.0004735199, 0.0032350094], [[3, 3, 2, 1, 2], 0, 0], [[3, 3, 2, 1, 3], 0, 0], [[3, 3, 2, 2, 1], 0.0019600511, 0], [[3, 3, 2, 2, 2], 0, 0], [[3, 3, 2, 2, 3], 0, 0], [[3, 3, 2, 3, 1], 0, 0], [[3, 3, 2, 3, 2], 0, 0], [[3, 3, 2, 3, 3], 0, 0], [[3, 3, 3, 1, 1], 0.0014679444, 0.0105738247], [[3, 3, 3, 1, 2], 0.0003518044, 0], [[3, 3, 3, 1, 3], 0, 0], [[3, 3, 3, 2, 1], 0, 0.0013931583], [[3, 3, 3, 2, 2], 0, 0], [[3, 3, 3, 2, 3], 0, 0], [[3, 3, 3, 3, 1], 0, 0.0001670449], [[3, 3, 3, 3, 2], 0, 0], [[3, 3, 3, 3, 3], 0, 0]]
n = 0
flag = 0
prev_state = []
prev_action = -1
list_of_actiontodict = ["null",{(1,1):0, (1,2):0}, {(1,1):0, (1,2):1}, {(1,1):1, (1,2):0}, {(1,1):1, (1,2):1}]
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
    if n > 20000:
        flag = 1
    extraline = 1


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