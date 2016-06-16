import map_init


def get_queue_len(internum):
    inter = map_init.intersections[internum]
    queue_len = []
    counter = 0
    for lane in inter.cars_queue:
        current_car = inter.cars_queue[lane]
        while current_car and current_car.speed <= 1:
            counter += 1
            current_car = current_car.next
        queue_len.append(counter)
    return queue_len
