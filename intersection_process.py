import macros
import car_define
import intersection_define
import map_init
import random

####list_of_vehicle
### add time_incre at the end of this function


def check_turn_and_change_lane(current_lane, current_inter, current_car):
    '''
    check turn and change lane action for current_car given current lane and current intersection
    '''

    if current_inter == current_car.my_path[-1]:  # already at destination
        if current_lane == macros.WESTL:
            if current_car.final_dir == macros.SOUTH:
                current_car.turn = macros.RIGHT
                current_car.change_lane = 1
            elif current_car.final_dir == macros.NORTH:
                current_car.turn = macros.LEFT
                current_car.change_lane = 0
            else:
                current_car.turn = macros.STRAIGHT
                current_car.change_lane = 0
        elif current_lane == macros.WESTR:
            if current_car.final_dir == macros.SOUTH:
                current_car.turn = macros.RIGHT
                current_car.change_lane = 0
            elif current_car.final_dir == macros.NORTH:
                current_car.turn = macros.LEFT
                current_car.change_lane = 1
            else:
                current_car.turn = macros.STRAIGHT
                current_car.change_lane = 0
        elif current_lane == macros.NORTHL:
            if current_car.final_dir == macros.WEST:
                current_car.turn = macros.RIGHT
                current_car.change_lane = 1
            elif current_car.final_dir == macros.EAST:
                current_car.turn = macros.LEFT
                current_car.change_lane = 0
            else:
                current_car.turn = macros.STRAIGHT
                current_car.change_lane = 0
        elif current_lane == macros.NORTHR:
            if current_car.final_dir == macros.WEST:
                current_car.turn = macros.RIGHT
                current_car.change_lane = 0
            elif current_car.final_dir == macros.EAST:
                current_car.turn = macros.LEFT
                current_car.change_lane = 1
            else:
                current_car.turn = macros.STRAIGHT
                current_car.change_lane = 0
        elif current_lane == macros.EASTL:
            if current_car.final_dir == macros.NORTH:
                current_car.turn = macros.RIGHT
                current_car.change_lane = 1
            elif current_car.final_dir == macros.SOUTH:
                current_car.turn = macros.LEFT
                current_car.change_lane = 0
            else:
                current_car.turn = macros.STRAIGHT
                current_car.change_lane = 0
        elif current_lane == macros.EASTR:
            if current_car.final_dir == macros.NORTH:
                current_car.turn = macros.RIGHT
                current_car.change_lane = 0
            elif current_car.final_dir == macros.SOUTH:
                current_car.turn = macros.LEFT
                current_car.change_lane = 1
            else:
                current_car.turn = macros.STRAIGHT
                current_car.change_lane = 0
        elif current_lane == macros.SOUTHL:
            if current_car.final_dir == macros.EAST:
                current_car.turn = macros.RIGHT
                current_car.change_lane = 1
            elif current_car.final_dir == macros.WEST:
                current_car.turn = macros.LEFT
                current_car.change_lane = 0
            else:
                current_car.turn = macros.STRAIGHT
                current_car.change_lane = 0
        elif current_lane == macros.SOUTHR:
            if current_car.final_dir == macros.EAST:
                current_car.turn = macros.RIGHT
                current_car.change_lane = 0
            elif current_car.final_dir == macros.WEST:
                current_car.turn = macros.LEFT
                current_car.change_lane = 1
            else:
                current_car.turn = macros.STRAIGHT
                current_car.change_lane = 0

    else:
        next_inter = (-1, -1)
        for i in range(0, len(current_car.my_path) - 1):  #decide if
            if current_inter == current_car.my_path[i]:
                next_inter = current_car.my_path[i + 1]
                break

        if next_inter == (-1, -1):
            print('shit!!!!!!!')
            return -1

        if current_lane == macros.WESTL:
            if next_inter[0] == current_inter[0] + 1:
                current_car.turn = macros.RIGHT
                current_car.change_lane = 1
            elif next_inter[0] == current_inter[0] - 1:
                current_car.turn = macros.LEFT
                current_car.change_lane = 0
            elif next_inter[1] == current_inter[1] + 1:
                current_car.turn = macros.STRAIGHT
                current_car.change_lane = 0
            else:
                print("You cannot make a U turn!!!!!!!")
                return -1
        elif current_lane == macros.WESTR:
            if next_inter[0] == current_inter[0] + 1:
                current_car.turn = macros.RIGHT
                current_car.change_lane = 0
            elif next_inter[0] == current_inter[0] - 1:
                current_car.turn = macros.LEFT
                current_car.change_lane = 1
            elif next_inter[1] == current_inter[1] + 1:
                current_car.turn = macros.STRAIGHT
                current_car.change_lane = 0
            else:
                print("You cannot make a U turn!!!!!!!")
                return -1
        elif current_lane == macros.NORTHL:
            if next_inter[1] == current_inter[1] - 1:
                current_car.turn = macros.RIGHT
                current_car.change_lane = 1
            elif next_inter[1] == current_inter[1] + 1:
                current_car.turn = macros.LEFT
                current_car.change_lane = 0
            elif next_inter[0] == current_inter[0] + 1:
                current_car.turn = macros.STRAIGHT
                current_car.change_lane = 0
            else:
                print("You cannot make a U turn!!!!!!!")
                return -1
        elif current_lane == macros.NORTHR:
            if next_inter[1] == current_inter[1] - 1:
                current_car.turn = macros.RIGHT
                current_car.change_lane = 0
            elif next_inter[1] == current_inter[1] + 1:
                current_car.turn = macros.LEFT
                current_car.change_lane = 1
            elif next_inter[0] == current_inter[0] + 1:
                current_car.turn = macros.STRAIGHT
                current_car.change_lane = 0
            else:
                print("You cannot make a U turn!!!!!!!")
                return -1
        elif current_lane == macros.EASTL:
            if next_inter[0] == current_inter[0] - 1:
                current_car.turn = macros.RIGHT
                current_car.change_lane = 1
            elif next_inter[0] == current_inter[0] + 1:
                current_car.turn = macros.LEFT
                current_car.change_lane = 0
            elif next_inter[1] == current_inter[1] - 1:
                current_car.turn = macros.STRAIGHT
                current_car.change_lane = 0
            else:
                print("You cannot make a U turn!!!!!!!")
                return -1
        elif current_lane == macros.EASTR:
            if next_inter[0] == current_inter[0] - 1:
                current_car.turn = macros.RIGHT
                current_car.change_lane = 0
            elif next_inter[0] == current_inter[0] + 1:
                current_car.turn = macros.LEFT
                current_car.change_lane = 1
            elif next_inter[1] == current_inter[1] - 1:
                current_car.turn = macros.STRAIGHT
                current_car.change_lane = 0
            else:
                print("You cannot make a U turn!!!!!!!")
                return -1
        elif current_lane == macros.SOUTHL:
            if next_inter[1] == current_inter[1] + 1:
                current_car.turn = macros.RIGHT
                current_car.change_lane = 1
            elif next_inter[1] == current_inter[1] - 1:
                current_car.turn = macros.LEFT
                current_car.change_lane = 0
            elif next_inter[0] == current_inter[0] - 1:
                current_car.turn = macros.STRAIGHT
                current_car.change_lane = 0
            else:
                print("You cannot make a U turn!!!!!!!")
                return -1
        elif current_lane == macros.SOUTHR:
            if next_inter[1] == current_inter[1] + 1:
                current_car.turn = macros.RIGHT
                current_car.change_lane = 0
            elif next_inter[1] == current_inter[1] - 1:
                current_car.turn = macros.LEFT
                current_car.change_lane = 1
            elif next_inter[0] == current_inter[0] - 1:
                current_car.turn = macros.STRAIGHT
                current_car.change_lane = 0
            else:
                print("You cannot make a U turn!!!!!!!")
                return -1
    return


def car_follow(current_car):
    if not current_car.prev:
        if current_car.speed < macros.CRUISE_SPEED:
            current_car.acc = macros.ACCELERATION
        else:
            current_car.speed = macros.CRUISE_SPEED
            current_car.acc = 0
    else:
        if current_car.position >= current_car.prev.position:
            current_car.position = current_car.prev.position - 0.1
            current_car.acc = macros.DECELERATION
        elif (current_car.prev.position - current_car.position) < macros.SAFE_DIST:
            current_car.acc = min(macros.DECELERATION, (current_car.prev.speed**2 - current_car.speed**2)/(2*(current_car.prev.position - current_car.position)))
        elif (current_car.prev.position - current_car.position) == macros.SAFE_DIST:
            current_car.acc = 0
        else:
            if current_car.speed < macros.CRUISE_SPEED:
                current_car.acc = macros.ACCELERATION
            else:
                current_car.speed = macros.CRUISE_SPEED
                current_car.acc = 0

    if current_car.next == current_car or current_car.prev == current_car:
        print('NEXT = CURRENT!!!!!!!')
        return -1
    return

def change_lane(side_lane_num, car, inter, current_lane):
    # -1 means turn left
    find_lagging_car = 0
    side_lane = inter.cars_queue[side_lane_num]
    current_side_lane_car = side_lane
    if car.position < car.speed * macros.CRITICAL_GAP:
        return

    while current_side_lane_car:
        if current_side_lane_car.position < car.position:
            find_lagging_car = 1
            lagging_car = current_side_lane_car
            if current_side_lane_car.prev:
                leading_car = current_side_lane_car.prev
                if (leading_car.position - lagging_car.position) >= macros.CRITICAL_GAP * car.speed \
                        and (car.position - lagging_car.position >= macros.SAFE_DIST or car.speed >= lagging_car.speed) \
                        and (leading_car.position - car.position >= macros.SAFE_DIST or leading_car.speed >= car.speed):
                    if not car.prev:
                        if not car.next:
                            inter.cars_queue[current_lane] = None
                            car.next = lagging_car
                            lagging_car.prev = car
                            car.prev = leading_car
                            leading_car.next = car
                        else:
                            inter.cars_queue[current_lane] = car.next
                            car.next.prev = None
                            car.next = lagging_car
                            lagging_car.prev = car
                            car.prev = leading_car
                            leading_car.next = car
                    else:
                        if not car.next:
                            car.prev.next = None
                            car.next = lagging_car
                            lagging_car.prev = car
                            car.prev = leading_car
                            leading_car.next = car
                        else:
                            car.prev.next = car.next
                            car.next.prev = car.prev
                            car.next = lagging_car
                            lagging_car.prev = car
                            car.prev = leading_car
                            leading_car.next = car

                else:
                    if not car.prev:
                        car.acc = macros.DECELERATION - random.random()
                    elif car.position >= car.prev.position:
                        car.acc = macros.DECELERATION
                        car.position = car.prev.position - 0.1
                    elif (car.prev.position - car.position) < macros.SAFE_DIST:
                        car.acc = min(macros.DECELERATION, (car.prev.speed**2 - car.speed**2)/(2*(car.prev.position - car.position))) - random.random()
                    else:
                        car.acc = macros.DECELERATION - random.random()
            else:
                if car.position - current_side_lane_car.position >= macros.SAFE_DIST or car.speed >= current_side_lane_car.speed:
                    if not car.prev:
                        if not car.next:
                            inter.cars_queue[side_lane_num] = car
                            inter.cars_queue[current_lane] = None
                            current_side_lane_car.prev = car
                            car.next = current_side_lane_car
                        else:
                            inter.cars_queue[current_lane] = car.next
                            inter.cars_queue[side_lane_num] = car
                            car.next.prev = None
                            current_side_lane_car.prev = car
                            car.next = current_side_lane_car
                    else:
                        if not car.next:
                            inter.cars_queue[side_lane_num] = car
                            car.prev.next = None
                            car.prev = None
                            current_side_lane_car.prev = car
                            car.next = current_side_lane_car
                        else:
                            inter.cars_queue[side_lane_num] = car
                            car.prev.next = car.next
                            car.next.prev = car.prev
                            car.prev = None
                            current_side_lane_car.prev = car
                            car.next = current_side_lane_car

                else:
                    if not car.prev:
                        car.acc = macros.DECELERATION - random.random()
                    elif car.position >= car.prev.position:
                        car.acc = macros.DECELERATION
                        car.position = car.prev.position - 0.1
                    elif (car.prev.position - car.position) < macros.SAFE_DIST:
                        car.acc = min(macros.DECELERATION, ((car.prev.speed**2 - car.speed**2)/(2*(car.prev.position - car.position)))) - random.random()
                    else:
                        car.acc = macros.DECELERATION - random.random()
            break
        if not current_side_lane_car.next:
            break
        current_side_lane_car = current_side_lane_car.next

    if find_lagging_car == 0:
        if not current_side_lane_car:
            if not car.prev:
                if not car.next:
                    inter.cars_queue[current_lane] = None
                    inter.cars_queue[side_lane_num] = car
                else:
                    inter.cars_queue[current_lane] = car.next
                    car.next.prev = None
                    car.next = None
                    inter.cars_queue[side_lane_num] = car
            else:
                if not car.next:
                    car.prev.next = None
                    car.prev = None
                    inter.cars_queue[side_lane_num] = car
                else:
                    car.prev.next = car.next
                    car.next.prev = car.prev
                    car.prev = None
                    car.next = None
                    inter.cars_queue[side_lane_num] = car
        else:
            if current_side_lane_car.position - car.position >= macros.SAFE_DIST or current_side_lane_car.speed >= car.speed:
                if not car.prev:
                    if not car.next:
                        inter.cars_queue[current_lane] = None
                        current_side_lane_car.next = car
                        car.prev = current_side_lane_car
                    else:
                        inter.cars_queue[current_lane] = car.next
                        car.next.prev = None
                        car.next = None
                        current_side_lane_car.next = car
                        car.prev = current_side_lane_car
                else:
                    if not car.next:
                        car.prev.next = None
                        current_side_lane_car.next = car
                        car.prev = current_side_lane_car
                    else:
                        car.prev.next = car.next
                        car.next.prev = car.prev
                        current_side_lane_car.next = car
                        car.prev = current_side_lane_car
                        car.next = None
            else:
                if not car.prev:
                    car.acc = macros.DECELERATION - random.random()
                elif car.position >= car.prev.position:
                    car.acc = macros.DECELERATION
                    car.position = car.prev.position - 0.1
                elif (car.prev.position - car.position) < macros.SAFE_DIST:
                    car.acc = min(macros.DECELERATION, (car.prev.speed**2 - car.speed**2)/(2*(car.prev.position - car.position))) - random.random()
                else:
                    car.acc = macros.DECELERATION - random.random()


def turn_left(car, opposite_left_lane, opposite_right_lane, intersection, opposite_len, target_lane, target_inter,
              current_length, current_lane):
    opposite_len = getattr(intersection, opposite_len)
    ol_ok = 0
    or_ok = 0
    opposite_left_car = intersection.cars_queue[opposite_left_lane]

    opposite_right_car = intersection.cars_queue[opposite_right_lane]
    target_intersection = getattr(intersection, target_inter)

    if current_length - car.position <= macros.DISTANCE_FROM_TRAFFIC_LIGHT and current_length - car.position > macros.OBSERVE_DISTANCE:
        car.acc = (4 - car.speed**2)/(2*(current_length - macros.OBSERVE_DISTANCE - car.position))

    if current_length - car.position <= macros.OBSERVE_DISTANCE:
        if not opposite_left_car or (opposite_len + 6 - opposite_left_car.position) >= 2 * opposite_left_car.speed:
            ol_ok = 1
        elif opposite_left_car.position >= opposite_len + 6 and (not opposite_left_car.next or opposite_len + 6 - opposite_left_car.next.position >= 2 * opposite_left_car.next.speed):
            ol_ok = 1
        if not opposite_right_car or (opposite_len + 6 - opposite_right_car.position) >= 2 * opposite_right_car.speed:
            or_ok = 1
        elif opposite_right_car.position >= opposite_len + 6 and (not opposite_right_car.next or opposite_len + 6 - opposite_right_car.next.position >= 3 * opposite_right_car.next.speed):
            or_ok = 1
        if ol_ok and or_ok:
            if target_intersection:
                target_intersection.append(target_lane, car)
                car.position = 0
            if car.next:
                intersection.cars_queue[current_lane] = car.next
                car.next.prev = None
                car.next = None
            else:
                intersection.cars_queue[current_lane] = None

        elif car.position >= current_length - 1:
            car.position = current_length
            car.speed = 0
            car.acc = 0
    return


def turn_right(car, intersection, target_lane, target_inter, current_length, current_lane):
    if car.position >= current_length - 1:
        target_intersection = getattr(intersection, target_inter)
        if car.prev:
            if car.next:
                car.prev.next = car.next
                car.next.prev = car.prev
            else:
                car.prev.next = None
        else:
            if car.next:
                intersection.cars_queue[current_lane] = car.next
                car.next.prev = None
            else:
                intersection.cars_queue[current_lane] = None

        if target_intersection:
            target_intersection.append(target_lane, car)
            car.position = 0
            car.next = None
        return


def get_needed_data(current_lane):
    if current_lane == macros.WESTL or current_lane == macros.WESTR:
        return (
            macros.EASTL, macros.EASTR, "east_len", macros.SOUTHL, "north", macros.NORTHR, "south", "west_len", "east")
    if current_lane == macros.EASTR or current_lane == macros.EASTL:
        return (
            macros.WESTL, macros.WESTR, "west_len", macros.NORTHL, "south", macros.SOUTHR, "north", "east_len", "west")
    if current_lane == macros.NORTHL or current_lane == macros.NORTHR:
        return (
            macros.SOUTHL, macros.SOUTHR, "south_len", macros.WESTL, "east", macros.EASTR, "west", "north_len", "south")
    if current_lane == macros.SOUTHR or current_lane == macros.SOUTHL:
        return (
            macros.NORTHL, macros.NORTHR, "north_len", macros.EASTL, "west", macros.WESTR, "east", "south_len",
            "north")


def process_one_lane(current_lane, current_inter_num, signal):
    '''
    process one lane, given the signal
    '''
    current_inter = map_init.intersections[current_inter_num]
    current_car = current_inter.cars_queue[current_lane]
    (opposite_left_lane, opposite_right_lane, opposite_len, left_target_lane, left_target_intersection,
     right_target_lane, right_target_intersection, current_len, straight_target) = get_needed_data(current_lane)
    current_length = getattr(current_inter, current_len)

    if signal == macros.GREEN:
        n=0
        while current_car:
            n+=1
            if n >= 40:
                current_inter.cars_queue[current_lane] = None
                return
            if current_car == current_car.next:
                current_car.next = None
                current_car.prev = None
                current_car = None
                current_inter.cars_queue[current_lane] = None
                return
            next_car = current_car.next
            if check_turn_and_change_lane(current_lane, current_inter_num, current_car) == -1:
                current_car.next = None
                current_car.prev = None
                current_car = None
                current_inter.cars_queue[current_lane] = None
                return
            i = [macros.WESTL, macros.EASTL, macros.NORTHL, macros.SOUTHL,
                 macros.WESTR, macros.EASTR, macros.NORTHR, macros.SOUTHR].index(current_lane)
            side_lane_num = [macros.WESTR, macros.EASTR, macros.NORTHR, macros.SOUTHR,
                         macros.WESTL, macros.EASTL, macros.NORTHL, macros.SOUTHL][i]

            if car_follow(current_car) == -1:
                current_car.next = None
                current_car.prev = None
                current_car = None
                current_inter.cars_queue[current_lane] = None
                continue
            if current_car.turn == macros.LEFT:
                if current_car.change_lane == 1:
                    change_lane(side_lane_num, current_car,current_inter,current_lane)
                    current_car.change_lane = 0
                else:
                    turn_left(current_car, opposite_left_lane, opposite_right_lane, current_inter, opposite_len,
                              left_target_lane, left_target_intersection, current_length, current_lane)

            elif current_car.turn == macros.RIGHT:
                if current_car.change_lane == 1:
                    change_lane(side_lane_num, current_car,current_inter,current_lane)
                    current_car.change_lane = 0
                else:
                    turn_right(current_car, current_inter, right_target_lane, right_target_intersection, current_length, current_lane)

            elif current_car.turn == macros.STRAIGHT:
                if current_car.position >= current_length:
                    straight_target_inter = getattr(current_inter, straight_target)
                    if straight_target_inter:
                        straight_target_inter.append(current_lane, current_car)
                        current_car.position = 0
                    if current_car.next:
                        current_inter.cars_queue[current_lane] = current_car.next
                        current_car.next.prev = None
                        current_car.next = None
                    else:
                        current_inter.cars_queue[current_lane] = None
                #if current_car.position >= current_length + 12:
                #    straight_target_inter = getattr(current_inter, straight_target)
                #    if straight_target_inter:
                #        straight_target_inter.append(current_lane, current_car)
                #        current_car.position = current_car.position - current_length - 12
                #    if current_car.next:
                #        current_inter.cars_queue[current_lane] = current_car.next
                #        current_car.next.prev = None
                #        current_car.next = None
                #    else:
                #        current_inter.cars_queue[current_lane] = None
            car_define.get_speed(current_car)
            car_define.get_position(current_car)
            current_car = next_car

    elif signal == macros.YELLOW:
        n=0
        while current_car:
            n += 1
            if n >= 40:
                current_inter.cars_queue[current_lane] = None
                return
            if current_car == current_car.next:
                current_car.next = None
                current_car.prev = None
                current_car = None
                current_inter.cars_queue[current_lane] = None
                return
            next_car = current_car.next
            if check_turn_and_change_lane(current_lane, current_inter_num, current_car) == -1:
                current_car.next = None
                current_car.prev = None
                current_car = None
                current_inter.cars_queue[current_lane] = None
                return
            i = [macros.WESTL, macros.EASTL, macros.NORTHL, macros.SOUTHL,
                 macros.WESTR, macros.EASTR, macros.NORTHR, macros.SOUTHR].index(current_lane)
            side_lane_num = [macros.WESTR, macros.EASTR, macros.NORTHR, macros.SOUTHR,
                         macros.WESTL, macros.EASTL, macros.NORTHL, macros.SOUTHL][i]

            if current_car.position > current_length:
                if current_car.turn == macros.LEFT:
                    if current_car.change_lane == 1:
                        print("there's a bug yellow left")
                        change_lane(side_lane_num, current_car, current_inter, current_lane)
                        current_car.change_lane = 0
                    else:
                        turn_left(current_car, opposite_left_lane, opposite_right_lane, current_inter, opposite_len,
                                  left_target_lane, left_target_intersection, current_length, current_lane)
                elif current_car.turn == macros.RIGHT:
                    if current_car.change_lane == 1:
                        print("there's a bug yellow right")
                        change_lane(side_lane_num, current_car, current_inter, current_lane)
                        current_car.change_lane = 0
                    else:
                        turn_right(current_car, current_inter, right_target_lane, right_target_intersection, current_length, current_lane)
                elif current_car.turn == macros.STRAIGHT:
                    straight_target_inter = getattr(current_inter, straight_target)
                    if straight_target_inter:
                        straight_target_inter.append(current_lane, current_car)
                        current_car.position = 0
                    if current_car.next:
                        current_inter.cars_queue[current_lane] = current_car.next
                        current_car.next.prev = None
                        current_car.next = None
                    else:
                        current_inter.cars_queue[current_lane] = None
                current_car.acc = macros.ACCELERATION

            else:
                if current_length - current_car.position > macros.DISTANCE_FROM_TRAFFIC_LIGHT:
                    if car_follow(current_car) == -1:
                        current_car.next = None
                        current_car.prev = None
                        current_car = None
                        current_inter.cars_queue[current_lane] = None
                        return

                else:
                    if not current_car.prev or current_car.prev.position > current_length:
                        if 1 < current_length - current_car.position <= macros.DISTANCE_FROM_TRAFFIC_LIGHT:
                            current_car.acc = (1 - current_car.speed ** 2) / (2 * (current_length - 1 - current_car.position))
                        elif 0 < current_length - current_car.position <= 1:
                            current_car.acc = -abs(current_car.speed ** 2 / (2 * (current_length - current_car.position)))
                        else:
                            current_car.acc = 0
                            current_car.speed = 0
                            current_car.position = current_length
                    elif current_car.position < current_car.prev.position - 1:
                        current_car.acc = -abs(current_car.speed ** 2 / (2 * (current_car.prev.position - current_car.position)))
                    else:
                        current_car.position = current_car.prev.position - 0.1
                        current_car.speed = 0
                        current_car.acc = 0
                if current_car.change_lane == 1:
                    change_lane(side_lane_num, current_car, current_inter, current_lane)
                    current_car.change_lane = 0

            car_define.get_speed(current_car)
            car_define.get_position(current_car)
            current_car = next_car

    elif signal == macros.RED:
        n=0
        while current_car:
            n += 1
            if n >= 40:
                current_inter.cars_queue[current_lane] = None
                return
            if current_car == current_car.next:
                current_car.next = None
                current_car.prev = None
                current_car = None
                current_inter.cars_queue[current_lane] = None
                return
            next_car = current_car.next
            if check_turn_and_change_lane(current_lane, current_inter_num, current_car) == -1:
                current_car.next = None
                current_car.prev = None
                current_car = None
                current_inter.cars_queue[current_lane] = None
                return
            i = [macros.WESTL, macros.EASTL, macros.NORTHL, macros.SOUTHL,
                 macros.WESTR, macros.EASTR, macros.NORTHR, macros.SOUTHR].index(current_lane)
            side_lane_num = [macros.WESTR, macros.EASTR, macros.NORTHR, macros.SOUTHR,
                         macros.WESTL, macros.EASTL, macros.NORTHL, macros.SOUTHL][i]

            if current_car.position > current_length:
                if current_car.turn == macros.LEFT:
                    if current_car.change_lane == 1:
                        print("there's a bug red left")
                        change_lane(side_lane_num, current_car, current_inter, current_lane)
                        current_car.change_lane = 0
                    else:
                        turn_left(current_car, opposite_left_lane, opposite_right_lane, current_inter, opposite_len,
                                  left_target_lane, left_target_intersection, current_length, current_lane)
                elif current_car.turn == macros.RIGHT:
                    if current_car.change_lane == 1:
                        print("here's a bug red right")
                        change_lane(side_lane_num, current_car, current_inter, current_lane)
                        current_car.change_lane = 0
                    else:
                        turn_right(current_car, current_inter, right_target_lane, right_target_intersection,
                                   current_length, current_lane)
                elif current_car.turn == macros.STRAIGHT:
                    straight_target_inter = getattr(current_inter, straight_target)
                    if straight_target_inter:
                        straight_target_inter.append(current_lane, current_car)
                        current_car.position = 0
                    if current_car.next:
                        current_inter.cars_queue[current_lane] = current_car.next
                        current_car.next.prev = None
                        current_car.next = None
                    else:
                        current_inter.cars_queue[current_lane] = None
                current_car.acc = macros.ACCELERATION

            if current_length - current_car.position > macros.DISTANCE_FROM_TRAFFIC_LIGHT:
                if car_follow(current_car) == -1:
                    current_car.next = None
                    current_car.prev = None
                    current_car = None
                    current_inter.cars_queue[current_lane] = None
                    return

            else:
                if not current_car.prev or current_car.prev.position > current_length:
                    if 1 < current_length - current_car.position <= macros.DISTANCE_FROM_TRAFFIC_LIGHT:
                        current_car.acc = (1 - current_car.speed ** 2) / (
                        2 * (current_length - 1 - current_car.position))
                    elif 0 < current_length - current_car.position <= 1:
                        current_car.acc = -abs(current_car.speed ** 2 / (2 * (current_length - current_car.position)))
                    else:
                        current_car.acc = 0
                        current_car.speed = 0
                        current_car.position = current_length
                elif current_car.position < current_car.prev.position - 1:
                    current_car.acc = -abs(current_car.speed ** 2 / (2 * (current_car.prev.position - current_car.position)))
                else:
                    current_car.position = current_car.prev.position - 0.1
                    current_car.speed = 0
                    current_car.acc = 0
            if current_car.change_lane == 1:
                change_lane(side_lane_num, current_car, current_inter, current_lane)
                current_car.change_lane = 0

            car_define.get_speed(current_car)
            car_define.get_position(current_car)
            current_car = next_car


def intersection_process(inter_num):
    inter = map_init.intersections[inter_num]
    dic_NSGREEN_EWRED = {macros.WESTL: macros.RED, macros.WESTR: macros.RED, macros.EASTL: macros.RED,
                         macros.EASTR: macros.RED, macros.NORTHL: macros.GREEN, macros.NORTHR: macros.GREEN,
                         macros.SOUTHR: macros.GREEN, macros.SOUTHL: macros.GREEN}
    dic_NSYELLOW_EWRED = {macros.WESTL: macros.RED, macros.WESTR: macros.RED, macros.EASTL: macros.RED,
                          macros.EASTR: macros.RED, macros.NORTHL: macros.YELLOW, macros.NORTHR: macros.YELLOW,
                          macros.SOUTHR: macros.YELLOW, macros.SOUTHL: macros.YELLOW}
    dic_NSRED_EWGREEN = {macros.WESTL: macros.GREEN, macros.WESTR: macros.GREEN, macros.EASTL: macros.GREEN,
                         macros.EASTR: macros.GREEN, macros.NORTHL: macros.RED, macros.NORTHR: macros.RED,
                         macros.SOUTHR: macros.RED, macros.SOUTHL: macros.RED}
    dic_NSRED_EWYELLOW = {macros.WESTL: macros.YELLOW, macros.WESTR: macros.YELLOW, macros.EASTL: macros.YELLOW,
                          macros.EASTR: macros.YELLOW, macros.NORTHL: macros.RED, macros.NORTHR: macros.RED,
                          macros.SOUTHR: macros.RED, macros.SOUTHL: macros.RED}
    dic = {macros.NSGREEN_EWRED: dic_NSGREEN_EWRED, macros.NSYELLOW_EWRED: dic_NSYELLOW_EWRED,
           macros.NSRED_EWGREEN: dic_NSRED_EWGREEN, macros.NSRED_EWYELLOW: dic_NSRED_EWYELLOW}
    for i in range(1, 9):
        signal = dic[inter.current_phase][i]
        process_one_lane(i, inter_num, signal)
        if map_init.intersections[inter_num].cars_queue[i]:
            map_init.intersections[inter_num].cars_queue[i].prev = None
    return

