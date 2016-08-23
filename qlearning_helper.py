import map_init
import macros


def get_queue_len(internum):
    inter = map_init.intersections[internum]
    queue_len = []
    for lane in inter.cars_queue:
        counter = 0
        current_car = inter.cars_queue[lane]
        while current_car and current_car.speed <= 2:
            counter += 1
            if current_car == current_car.next:
                print('Current = Next')
                current_car.next = None
            current_car = current_car.next
        queue_len.append(counter)
    return queue_len


def get_first_coherence_list():
    coherence_matrix = []
    for i in range(1, len(macros.VER_DIM)):
        for j in range(1, len(macros.HOR_DIM)):
            inter = map_init.intersections[(i,j)]
            coherence_list = []
            for k in range(1, len(macros.VER_DIM)):
                for l in range(1, len(macros.HOR_DIM)):
                    loop_inter = map_init.intersections[(k,l)]
                    if loop_inter == inter.west:
                        tot = get_queue_length(inter.cars_queue[macros.WESTL]) + get_queue_length(inter.cars_queue[macros.WESTR]) + get_queue_length(loop_inter.cars_queue[macros.EASTL]) + get_queue_length(loop_inter.cars_queue[macros.EASTR])
                        coherence_list.append(tot)
                    elif loop_inter == inter.east:
                        tot = get_queue_length(inter.cars_queue[macros.EASTL]) + get_queue_length(inter.cars_queue[macros.EASTR]) + get_queue_length(loop_inter.cars_queue[macros.WESTL]) + get_queue_length(loop_inter.cars_queue[macros.WESTR])
                        coherence_list.append(tot)
                    elif loop_inter == inter.north:
                        tot = get_queue_length(inter.cars_queue[macros.NORTHL]) + get_queue_length(inter.cars_queue[macros.NORTHR]) + get_queue_length(loop_inter.cars_queue[macros.SOUTHL]) + get_queue_length(loop_inter.cars_queue[macros.SOUTHR])
                        coherence_list.append(tot)
                    elif loop_inter == inter.south:
                        tot = get_queue_length(inter.cars_queue[macros.SOUTHL]) + get_queue_length(inter.cars_queue[macros.SOUTHR]) + get_queue_length(loop_inter.cars_queue[macros.NORTHL]) + get_queue_length(loop_inter.cars_queue[macros.NORTHR])
                        coherence_list.append(tot)
                    else:
                        coherence_list.append(-1)
            coherence_matrix.append(coherence_list)
    macros.prev_coherence_matrix = coherence_matrix


def get_coherence_list():
    coherence_matrix = []
    for i in range(1, len(macros.VER_DIM)):
        for j in range(1, len(macros.HOR_DIM)):
            inter = map_init.intersections[(i,j)]
            coherence_list = []
            for k in range(1, len(macros.VER_DIM)):
                for l in range(1, len(macros.HOR_DIM)):
                    loop_inter = map_init.intersections[(k,l)]
                    if loop_inter == inter.west:
                        tot = get_queue_length(inter.cars_queue[macros.WESTL]) + get_queue_length(inter.cars_queue[macros.WESTR]) + get_queue_length(loop_inter.cars_queue[macros.EASTL]) + get_queue_length(loop_inter.cars_queue[macros.EASTR])
                        coherence_list.append(tot)
                    elif loop_inter == inter.east:
                        tot = get_queue_length(inter.cars_queue[macros.EASTL]) + get_queue_length(inter.cars_queue[macros.EASTR]) + get_queue_length(loop_inter.cars_queue[macros.WESTL]) + get_queue_length(loop_inter.cars_queue[macros.WESTR])
                        coherence_list.append(tot)
                    elif loop_inter == inter.north:
                        tot = get_queue_length(inter.cars_queue[macros.NORTHL]) + get_queue_length(inter.cars_queue[macros.NORTHR]) + get_queue_length(loop_inter.cars_queue[macros.SOUTHL]) + get_queue_length(loop_inter.cars_queue[macros.SOUTHR])
                        coherence_list.append(tot)
                    elif loop_inter == inter.south:
                        tot = get_queue_length(inter.cars_queue[macros.SOUTHL]) + get_queue_length(inter.cars_queue[macros.SOUTHR]) + get_queue_length(loop_inter.cars_queue[macros.NORTHL]) + get_queue_length(loop_inter.cars_queue[macros.NORTHR])
                        coherence_list.append(tot)
                    else:
                        coherence_list.append(-1)
            coherence_matrix.append(coherence_list)
    merge_coh_matrices(coherence_matrix)


def merge_coh_matrices(coherence_matrix):
    for i in range(0, len(macros.prev_coherence_matrix)):
        for j in range(0, len(macros.prev_coherence_matrix[0])):
            macros.prev_coherence_matrix[i][j] = (macros.prev_coherence_matrix[i][j] + coherence_matrix[i][j]) / 2


def get_queue_length(queue):
    length = 0
    while queue:
        queue = queue.next
        length += 1
    return length

