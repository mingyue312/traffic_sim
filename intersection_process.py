import macros
import car_define
import intersection_define

####list_of_vehicle
### add time_incre at the end of this function



def check_turn_and_change_lane(current_lane, current_inter, current_car):
    '''
    check turn and change lane action for current_car given current lane and current intersection
    '''

    if current_inter == current_car.my_path[-1]:    # already at destination
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
        for i in range(0, len(current_car.my_path)-1):  #decide if
            if current_inter == current_car.my_path[i]:
                next_inter = current_car.my_path[i+1]
                break
            else:
                print("A car is not on its path!!!!!!")
                return -1

        if current_lane == macros.WESTL:
            if next_inter[0] == current_inter[0]+1:
                current_car.turn = macros.RIGHT
                current_car.change_lane = 1
            elif next_inter[0] == current_inter[0]-1:
                current_car.turn = macros.LEFT
                current_car.change_lane = 0
            elif next_inter[1] == current_inter[1]+1:
                current_car.turn = macros.STRAIGHT
                current_car.change_lane = 0
            else:
                print("You cannot make a U turn!!!!!!!")
                return -1
        elif current_lane == macros.WESTR:
            if next_inter[0] == current_inter[0]+1:
                current_car.turn = macros.RIGHT
                current_car.change_lane = 0
            elif next_inter[0] == current_inter[0]-1:
                current_car.turn = macros.LEFT
                current_car.change_lane = 1
            elif next_inter[1] == current_inter[1]+1:
                current_car.turn = macros.STRAIGHT
                current_car.change_lane = 0
            else:
                print("You cannot make a U turn!!!!!!!")
                return -1
        elif current_lane == macros.NORTHL:
            if next_inter[1] == current_inter[1]-1:
                current_car.turn = macros.RIGHT
                current_car.change_lane = 1
            elif next_inter[1] == current_inter[1]+1:
                current_car.turn = macros.LEFT
                current_car.change_lane = 0
            elif next_inter[0] == current_inter[0]+1:
                current_car.turn = macros.STRAIGHT
                current_car.change_lane = 0
            else:
                print("You cannot make a U turn!!!!!!!")
                return -1
        elif current_lane == macros.NORTHR:
            if next_inter[1] == current_inter[1]-1:
                current_car.turn = macros.RIGHT
                current_car.change_lane = 0
            elif next_inter[1] == current_inter[1]+1:
                current_car.turn = macros.LEFT
                current_car.change_lane = 1
            elif next_inter[0] == current_inter[0]+1:
                current_car.turn = macros.STRAIGHT
                current_car.change_lane = 0
            else:
                print("You cannot make a U turn!!!!!!!")
                return -1
        elif current_lane == macros.EASTL:
            if next_inter[0] == current_inter[0]+1:
                current_car.turn = macros.RIGHT
                current_car.change_lane = 1
            elif next_inter[0] == current_inter[0]-1:
                current_car.turn = macros.LEFT
                current_car.change_lane = 0
            elif next_inter[1] == current_inter[1]-1:
                current_car.turn = macros.STRAIGHT
                current_car.change_lane = 0
            else:
                print("You cannot make a U turn!!!!!!!")
                return -1
        elif current_lane == macros.EASTR:
            if next_inter[0] == current_inter[0]+1:
                current_car.turn = macros.RIGHT
                current_car.change_lane = 0
            elif next_inter[0] == current_inter[0]-1:
                current_car.turn = macros.LEFT
                current_car.change_lane = 1
            elif next_inter[1] == current_inter[1]-1:
                current_car.turn = macros.STRAIGHT
                current_car.change_lane = 0
            else:
                print("You cannot make a U turn!!!!!!!")
                return -1
        elif current_lane == macros.SOUTHL:
            if next_inter[1] == current_inter[1]+1:
                current_car.turn = macros.RIGHT
                current_car.change_lane = 1
            elif next_inter[1] == current_inter[1]-1:
                current_car.turn = macros.LEFT
                current_car.change_lane = 0
            elif next_inter[0] == current_inter[0]+1:
                current_car.turn = macros.STRAIGHT
                current_car.change_lane = 0
            else:
                print("You cannot make a U turn!!!!!!!")
                return -1
        elif current_lane == macros.SOUTHR:
            if next_inter[1] == current_inter[1]-1:
                current_car.turn = macros.RIGHT
                current_car.change_lane = 0
            elif next_inter[1] == current_inter[1]+1:
                current_car.turn = macros.LEFT
                current_car.change_lane = 1
            elif next_inter[0] == current_inter[0]+1:
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
         if (current_car.prev.location - current_car.location) < macros.SAFE_DIST:
             current_car.acc = macros.DECELERATION
         elif (current_car.prev.location - current_car.location) == macros.SAFE_DIST:
             current_car.acc = 0
         else:
             if current_car.speed < macros.CRUISE_SPEED:
                current_car.acc = macros.ACCELERATION
             else:
                 current_car.speed = macros.CRUISE_SPEED
                 current_car.acc = 0

def change_lane(side_lane, car):
    ##1 means turn left
    find_lagging_car = 0
    current_side_lane_car = side_lane
    while current_side_lane_car:
        if current_side_lane_car.position < car.position:
            find_lagging_car = 1
            lagging_car = current_side_lane_car
            if current_side_lane_car.prev:
                leading_car = current_side_lane_car.prev
                if (leading_car.position - lagging_car.position)/car.speed > macros.CRITICAL_GAP:
                    car.prev.next = car.next
                    car.next.prev = car.prev
                    car.next = lagging_car
                    lagging_car.prev = car
                    car.prev = leading_car
                    leading_car.next = car
                else:
                    car.acc = macros.DECELERATION
            else:
                current_side_lane_car.prev = car
                car.prev.next = car.next
                car.next.prev = car.prev
                car.next = current_side_lane_car
            break
        if not current_side_lane_car.next:
            break
        current_side_lane_car = current_side_lane_car.next


    if find_lagging_car == 0:
        car.prev.next = car.next
        car.next.prev = car.prev
        car.prev = current_side_lane_car


def turn_left(car,opposite_left_lane,opposite_right_lane,intersection,opposite_len,target_lane,target_inter,current_length):
    opposite_len = getattr(intersection,opposite_len)

    opposite_left_car = intersection.cars_queue[opposite_left_lane]
    opposite_right_car = intersection.cars_queue[opposite_right_lane]
    target_intersection = getattr(intersection,target_inter)

    if car.position <= macros.DISTANCE_FROM_TRAFFIC_LIGHT:
        car.acc = car.speed^2/(2*(current_length-car.position))
    if car.position <= macros.OBSERVE_DISTANCE:
        if((opposite_len + 6 - opposite_left_car.location)/opposite_left_car.speed >= 2 or
        (opposite_left_car.location >= opposite_len + 6 and (opposite_left_car.location - opposite_left_car.next.location)/opposite_left_car.next.speed >=2)) and\
        ((opposite_len + 6 - opposite_right_car.location)/opposite_right_car.speed >= 3 or
        (opposite_right_car.location >= opposite_len + 6 and (opposite_right_car.location - opposite_right_car.next.location)/opposite_right_car.next.speed >=3)):
            target_intersection.append(target_lane,car)
            car.next.prev = None
    return

def turn_right(car,intersection,target_lane,target_inter):
    target_intersection = getattr(intersection,target_inter)
    car.next.prev = None
    target_intersection.append(target_lane,car)
    return

def get_needed_data(current_lane):
    if current_lane == macros.WESTL or current_lane == macros.WESTR:
        return (macros.EASTL,macros.EASTR,"east_len",macros.SOUTHL,"south",macros.NORTHR,"north","west_len","east")
    if current_lane == macros.EASTR or current_lane == macros.EASTL:
        return (macros.WESTL,macros.WESTR,"west_len",macros.NORTHL,"west",macros.SOUTHR,"south","east_len","west")
    if current_lane == macros.NORTHL or current_lane == macros.NORTHR:
        return (macros.SOUTHL,macros.SOUTHR,"south_len",macros.WESTL,"south",macros.EASTR,"east","north_len","south")
    if current_lane == macros.SOUTHR or current_lane == macros.SOUTHL:
        return (macros.NORTHL,macros.NORTHR,"north_len",macros.EASTL,"north",macros.WESTR,"west","south_len","north")

def process_one_lane(current_lane, current_inter, signal):
    '''
    process one lane, given the signal
    '''

    current_car = current_inter.cars_queue[current_lane]
    (opposite_left_lane,opposite_right_lane,opposite_len,left_target_lane,left_target_intersection,right_target_lane,right_target_intersection,current_len,straight_target) = get_needed_data(current_lane)
    current_length = getattr(current_inter, current_len)

    if signal == macros.GREEN:
        while current_car:
            check_turn_and_change_lane(current_lane, current_inter, current_car)
            i = [macros.WESTL, macros.EASTL, macros.NORTHL, macros.SOUTHL,
                 macros.WESTR, macros.EASTR, macros.NORTHR, macros.SOUTHR].index(current_lane)
            side_lane = [macros.WESTR, macros.EASTR, macros.NORTHR, macros.SOUTHR,
                         macros.WESTL, macros.EASTL, macros.NORTHL, macros.SOUTHL][i]

            car_follow(current_car)
            if current_car.turn == macros.LEFT:
                if current_car.change_lane == 1:
                    change_lane(current_inter.cars_queue[side_lane],current_car)
                    current_car.change_lane = 0
                else:
                    turn_left(current_car,opposite_left_lane,opposite_right_lane,current_inter,opposite_len,left_target_lane,left_target_intersection,current_length)

            if current_car.turn == macros.RIGHT:
                if current_car.change_lane ==1:
                    change_lane(current_inter.cars_queue[side_lane],current_car)
                    current_car.change_lane = 0
                else:
                    turn_right(current_car,current_inter,right_target_intersection,right_target_lane)

            car_define.get_speed(current_car)
            car_define.get_position(current_car)

            if current_car.position >= current_length +12:
                straight_target_inter = getattr(current_inter,straight_target)
                straight_target_inter.append(current_lane,current_car)
                current_car.next.prev = None
            current_car = current_car.next

    elif signal == macros.YELLOW:

        while current_car:
            if current_car.location > current_length:
                car_follow(current_car)

            else:
                if current_car.prev.position > current_length or current_car.prev == None:
                    current_car.acc = current_car.speed^2/(2*(current_length-current_car.position))
                else:
                    current_car.acc = current_car.speed^2/(2*(current_car.prev.position - macros.LENGTHE_CAR - current_car.position))

            car_define.get_speed(current_car)
            car_define.get_position(current_car)

            current_car = current_car.next

    elif signal  == macros.RED:

        while current_car:
            if current_car.prev == None:
                current_car.acc = current_car.speed^2/(2*(current_length-current_car.position))
            else:
                current_car.acc = current_car.speed^2/(2*(current_car.prev.position - macros.LENGTHE_CAR - current_car.position))

            car_define.get_speed(current_car)
            car_define.get_position(current_car)
            current_car = current_car.next

def intersection_process(inter):
    dic_NSGREEN_EWRED = {macros.WESTL:macros.RED, macros.WESTR:macros.RED,macros.EASTL:macros.RED,macros.EASTR:macros.RED,macros.NORTHL:macros.GREEN,macros.NORTHR:macros.GREEN,macros.SOUTHR:macros.GREEN,macros.SOUTHL:macros.GREEN}
    dic_NSYELLOW_EWRED = {macros.WESTL:macros.RED, macros.WESTR:macros.RED,macros.EASTL:macros.RED,macros.EASTR:macros.RED,macros.NORTHL:macros.YELLOW,macros.NORTHR:macros.YELLOW,macros.SOUTHR:macros.YELLOW,macros.SOUTHL:macros.YELLOW}
    dic_NSRED_EWGREEN = {macros.WESTL:macros.GREEN, macros.WESTR:macros.GREEN,macros.EASTL:macros.GREEN,macros.EASTR:macros.GREEN,macros.NORTHL:macros.RED,macros.NORTHR:macros.RED,macros.SOUTHR:macros.RED,macros.SOUTHL:macros.RED}
    dic_NSRED_EWYELLOW = {macros.WESTL:macros.YELLOW, macros.WESTR:macros.YELLOW,macros.EASTL:macros.YELLOW,macros.EASTR:macros.YELLOW,macros.NORTHL:macros.RED,macros.NORTHR:macros.RED,macros.SOUTHR:macros.RED,macros.SOUTHL:macros.RED}
    dic = {macros.NSGREEN_EWRED:dic_NSGREEN_EWRED,macros.NSYELLOW_EWRED:dic_NSYELLOW_EWRED,macros.NSRED_EWGREEN:dic_NSRED_EWGREEN,macros.NSRED_EWYELLOW:dic_NSRED_EWYELLOW}
    for i in range(1,9):

        signal = dic[inter.current_phase][i]
        process_one_lane(i,inter,signal)
    return

