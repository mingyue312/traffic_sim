import intersection
import macros
import random
intersections = {}


def map_init():
    """

    """
    for i in range(1, len(macros.VER_DIM)):
        for j in range(1, len(macros.HOR_DIM)):
            intersections[(i, j)] = intersection.Intersection((i, j), macros.VER_DIM[i-1], macros.VER_DIM[i],
                                                              macros.HOR_DIM[j-1], macros.HOR_DIM[j])

    for inter in intersections:
        posx = macros.VER_DIM[0] + 2 * macros.LANE_WIDTH
        posy = macros.HOR_DIM[0] + 2 * macros.LANE_WIDTH
        for i in range(1, inter[0]):
            posx += macros.HOR_DIM[i]
            posx += 2 * macros.LANE_WIDTH
        for j in range(1, inter[1]):
            posy += macros.VER_DIM[j]
            posy += 2 * macros.LANE_WIDTH

    for inter_o in intersections:
        for inter_i in intersections:
            if inter_i[0] == inter_o[0] and inter_i[1] == inter_o[1] + 1:
                intersections[inter_o].east = intersections[inter_i]
                intersections[inter_i].west = intersections[inter_o]
            elif inter_i[1] == inter_o[1] and inter_i[0] == inter_o[0] + 1:
                intersections[inter_o].south = intersections[inter_i]
                intersections[inter_i].north = intersections[inter_o]

    # decide which intersections represent a boundary and which side is the boundary
    # random function gives the next arrival time of each lane
    # TODO: update for exponential arrival time
    for inter in intersections:
        if not intersections[inter].east:
            intersections[inter].boundary[macros.EASTL] = round(random.uniform(0, macros.FREQ), 2)
            intersections[inter].boundary[macros.EASTR] = round(random.uniform(0, macros.FREQ), 2)
        if not intersections[inter].west:
            intersections[inter].boundary[macros.WESTL] = round(random.uniform(0, macros.FREQ), 2)
            intersections[inter].boundary[macros.WESTR] = round(random.uniform(0, macros.FREQ), 2)
        if not intersections[inter].north:
            intersections[inter].boundary[macros.NORTHL] = round(random.uniform(0, macros.FREQ), 2)
            intersections[inter].boundary[macros.NORTHR] = round(random.uniform(0, macros.FREQ), 2)
        if not intersections[inter].south:
            intersections[inter].boundary[macros.SOUTHL] = round(random.uniform(0, macros.FREQ), 2)
            intersections[inter].boundary[macros.SOUTHR] = round(random.uniform(0, macros.FREQ), 2)

    return intersections


def is_exit(inter, dir):
    if dir == macros.WEST and inter[1] == 1:
        return True
    if dir == macros.EAST and inter[1] == len(macros.HOR_DIM)-1:
        return True
    if dir == macros.NORTH and inter[0] == 1:
        return True
    if dir == macros.SOUTH and inter[0] == len(macros.VER_DIM)-1:
        return True
    return False

map_init()