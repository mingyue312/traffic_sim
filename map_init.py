import intersection
import macros


def map_init():
    """

    """
    intersections = {}
    for i in range(1, len(macros.VER_DIM)):
        for j in range(1, len(macros.HOR_DIM)):
            intersections[(i, j)] = intersection.Intersection((i, j), macros.VER_DIM[i-1], macros.VER_DIM[i],
                                                              macros.HOR_DIM[j-1], macros.HOR_DIM[j])
            print intersections

    for inter_o in intersections:
        for inter_i in intersections:
            if inter_i[0] == inter_o[0] and inter_i[1] == inter_o[1] + 1:
                intersections[inter_o].east = intersections[inter_i]
                intersections[inter_i].west = intersections[inter_o]
            elif inter_i[1] == inter_o[1] and inter_i[0] == inter_o[0] + 1:
                intersections[inter_o].south = intersections[inter_i]
                intersections[inter_i].north = intersections[inter_o]

    return intersections

