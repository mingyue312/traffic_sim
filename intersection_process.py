import macros
import map_init
import car

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

def append(link_list,target):
    current = link_list
    if current:
        while current.next != None:
            current = current.next
        current.next = target
    else:
        link_list = target


def turn_left(car,opposite_left_lane,opposite_right_lane,intersection,opposite_len,target_lane,target_inter):
    len = getattr(intersection,opposite_len)
    opposite_left_car = intersection.cars_queue[opposite_left_lane]
    opposite_right_car = intersection.cars_queue[opposite_right_lane]
    target_intersection = getattr(intersection,target_inter)

    if car.position <= macros.DISTANCE_FROM_TRAFFIC_LIGHT:
        car.acc = car.speed^2/(2*car.position)
    if car.position <= macros.OBSERVE_DISTANCE:
        if((len + 6 - opposite_left_car.location)/opposite_left_car.speed >= 2 or \
        (opposite_left_car.location >= len + 6 and (opposite_left_car.location - opposite_left_car.next.location)/opposite_left_car.next.speed >=2)) and\
        ((len + 6 - opposite_right_car.location)/opposite_right_car.speed >= 3 or \
        (opposite_right_car.location >= len + 6 and (opposite_right_car.location - opposite_right_car.next.location)/opposite_right_car.next.speed >=3)):
            append(target_intersection.cars_queue[target_lane],car)
            car.next.prev = None
    return

def turn_right(car,intersection,target_lane,target_inter):
    target_intersection = getattr(intersection,target_inter)
    car.next.prev = None
    append(target_intersection.cars_queue[target_lane],car)
    return

def get_needed_data(current_lane):
    if current_lane == macros.WESTL or current_lane == macros.WESTR:
        return (macros.EASTL,macros.EASTR,"east_len",macros.SOUTHL,"south",macros.NORTHR,"north","west_len")
    if current_lane == macros.EASTR or current_lane == macros.EASTL:
        return (macros.WESTL,macros.WESTR,"west_len",macros.NORTHL,"west",macros.SOUTHR,"south","east_len")
    if current_lane == macros.NORTHL or current_lane == macros.NORTHR:
        return (macros.SOUTHL,macros.SOUTHR,"south_len",macros.WESTL,"south",macros.EASTR,"east","north_len")
    if current_lane == macros.SOUTHR or current_lane == macros.SOUTHL:
        return (macros.NORTHL,macros.NORTHR,"north_len",macros.EASTL,"north",macros.WESTR,"west","south_len")

def process_one_lane(current_lane, current_inter, cars_list, signal):
    '''
    process one lane, given the signal
    '''

    current_car = cars_list

    if signal == macros.GREEN:
        while current_car:
            check_turn_and_change_lane(current_lane, current_inter, current_car)
            i = [macros.WESTL, macros.EASTL, macros.NORTHL, macros.SOUTHL,
                 macros.WESTR, macros.EASTR, macros.NORTHR, macros.SOUTHR].index(current_lane)
            side_lane = [macros.WESTR, macros.EASTR, macros.NORTHR, macros.SOUTHR,
                         macros.WESTL, macros.EASTL, macros.NORTHL, macros.SOUTHL][i]
            (opposite_left_lane,opposite_right_lane,opposite_len,left_target_lane,left_target_intersection,right_target_lane,right_target_intersection) = get_needed_data(current_lane)

            car_follow(current_car)
            if current_car.turn == macros.LEFT:
                if current_car.change_lane == 1:
                    change_lane(current_inter.cars_queue[side_lane],current_car)
                    current_car.change_lane = 0
                else:
                    turn_left(current_car,opposite_left_lane,opposite_right_lane,current_inter,opposite_len,left_target_lane,left_target_intersection)

            if current_car.turn == macros.RIGHT:
                if current_car.change_lane ==1:
                    change_lane(current_inter.cars_queue[side_lane],current_car)
                    current_car.change_lane = 0
                else:
                    turn_right(current_car,current_inter,right_target_intersection,right_target_lane)

            current_car = current_car.next

    if signal == macros.YELLOW:
        (noneed,noneed,noneed,noneed,noneed,noneed,noneed,current_len) = get_needed_data(current_lane)
        len = getattr(current_inter, current_len)

        while current_car:
            if current_car.location > len:
                car_follow(current_car)
            current_car = current_car.next

def intersection_process(inter,action,):
    return
