
list = []
l2 = ['nul', 0,0.5,1]
l3 = ['nul', 0, 1]
for i in range(1,4):
    for j in range(1, 4):
        for k in range(1, 4):
            for l in range(1, 4):
                for m in range(1,3):
                    for n in range(1, 3):
                        for o in range(1, 3):
                            for p in range(1, 3):
                                list.append([l2[i],l2[j],l2[k],l2[l],l3[m],l3[n],l3[o],l3[p]])

def findindex(jointstate):
    #does this use 123 or 0,0.5,1/0,1???
    index = jointstate[7]+jointstate[6]*2+jointstate[5]*4+jointstate[4]*8+jointstate[3]*32+jointstate[2]*32*3+jointstate[1]*32*9+jointstate[0]*32*27
    return index

extraline =1