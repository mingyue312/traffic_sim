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
    for inter_o in intersections:
        for inter_i in intersections:
            if inter_i[0] == inter_o[0] and inter_i[1] == inter_o[1] + 1:
                intersections[inter_o].east = intersections[inter_i]
                intersections[inter_i].west = intersections[inter_o]
            elif inter_i[1] == inter_o[1] and inter_i[0] == inter_o[0] + 1:
                intersections[inter_o].south = intersections[inter_i]
                intersections[inter_i].north = intersections[inter_o]

    # decide which intersections represent a boundary and which side is the boundary
    # random function gives the arrival time and next arrival time of the car
    # TODO: update for exponential arrival time
    for inter in intersections:
        if not intersections[inter].east:
            intersections[inter].boundary[macros.EASTL] = [round(random.uniform(0, macros.FREQ), 2), round(random.uniform(macros.FREQ, macros.FREQ * 2),2)]
            intersections[inter].boundary[macros.EASTR] = [round(random.uniform(0, macros.FREQ), 2), round(random.uniform(macros.FREQ, macros.FREQ * 2),2)]
        if not intersections[inter].west:
            intersections[inter].boundary[macros.WESTL] = [round(random.uniform(0, macros.FREQ), 2), round(random.uniform(macros.FREQ, macros.FREQ * 2),2)]
            intersections[inter].boundary[macros.WESTR] = [round(random.uniform(0, macros.FREQ), 2), round(random.uniform(macros.FREQ, macros.FREQ * 2),2)]
        if not intersections[inter].north:
            intersections[inter].boundary[macros.NORTHL] = [round(random.uniform(0, macros.FREQ), 2), round(random.uniform(macros.FREQ, macros.FREQ * 2),2)]
            intersections[inter].boundary[macros.NORTHR] = [round(random.uniform(0, macros.FREQ), 2), round(random.uniform(macros.FREQ, macros.FREQ * 2),2)]
        if not intersections[inter].south:
            intersections[inter].boundary[macros.SOUTHL] = [round(random.uniform(0, macros.FREQ), 2), round(random.uniform(macros.FREQ, macros.FREQ * 2),2)]
            intersections[inter].boundary[macros.SOUTHR] = [round(random.uniform(0, macros.FREQ), 2), round(random.uniform(macros.FREQ, macros.FREQ * 2),2)]

    return intersections

