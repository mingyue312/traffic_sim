import macros
import map_init
import random


def find_path(init, fin):
    '''
    initial_ent: the intersection of initial entrance, example: intersection (1,1)
    final_exit: the intersection of final exit, example: intersection (1,3)
    '''
    path = []

    if init == fin:
        return init
    
    if init[0] == fin[0]:          # only need to travel horizontally
        if fin[1] > init[1]:       # move right
            for i in range(init[1], fin[1]+1):
                path.append((init[0], i))
        else:                       # move left
            for i in range(init[1], fin[1]-1, -1):
                path.append((init[0], i))

    elif init[1] == fin[1]:        # only need to travel vertically
        if fin[0] > init[0]:       # move down
            for i in range(init[0], fin[0]+1):
                path.append((i, init[1]))
        else:                      # move up
            for i in range(init[0], fin[0]-1, -1):
                path.append((i, init[1]))

    else:                          # need to travel both horizontally and vertically
        if fin[0] > init[0] and fin[1] > init[1]:   # to right and down
            if random.randint(0,1):                 # right then down
                for i in range(init[1], fin[1]+1):
                    path.append((init[0], i))
                for i in range(init[0]+1, fin[0]+1):
                    path.append((i, fin[1]))
            else:                                   # down then right
                for i in range(init[0], fin[0]+1):
                    path.append((i, init[1]))
                for i in range(init[1]+1, fin[1]+1):
                    path.append((fin[0], i))

        elif fin[0] < init[0] and fin[1] > init[1]: # to right and up
            if random.randint(0,1):                 # right then up
                for i in range(init[1], fin[1]+1):
                    path.append((init[0], i))
                for i in range(init[0]-1, fin[0]-1, -1):
                    path.append((i, fin[1]))
            else:                                   # up then right
                for i in range(init[0], fin[0]-1, -1):
                    path.append((i, init[1]))
                for i in range(init[1]+1, fin[1]+1):
                    path.append((fin[0], i))

        elif fin[0] > init[0] and fin[1] < init[1]: # to left and down
            if random.randint(0,1):                 # left then down
                for i in range(init[1], fin[1]-1, -1):
                    path.append((init[0], i))
                for i in range(init[0]+1, fin[0]+1):
                    path.append((i, fin[1]))
            else:                                   # down the left
                for i in range(init[0], fin[0]+1):
                    path.append((i, init[1]))
                for i in range(init[1]-1, fin[1]-1, -1):
                    path.append((fin[0], i))
        else:                                       # to left and up
            if random.randint(0,1):                 # left then up
                for i in range(init[1], fin[1]-1, -1):
                    path.append((init[0], i))
                for i in range(init[0]-1, fin[0]-1, -1):
                    path.append((i, fin[1]))
            else:                                   # up then left
                for i in range(init[0], fin[0]-1, -1):
                    path.append((i, init[1]))
                for i in range(init[1]-1, fin[1]-1, -1):
                    path.append((fin[0], i))

    return path


print(find_path((1,1),(1,1)))