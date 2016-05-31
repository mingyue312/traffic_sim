import macros

####list_of_vehicle
### add time_incre at the end of this function

def intersection_process(intersection, dic, list_of_vehicle):
    if intersection.phase_dictionary[intersection.current_phase] > intersection.reference_dictionary[intersection.current_phase]:
        intersection.phase_dictionary[intersection.current_phase] = 0

        if intersection.current_phase + 1 > 6:
            intersection.current_phase = 0

        else:
            intersection.current_phase = intersection.current_phase + 1

    if intersection.current_phase == 1 or intersection.current_phase == 4:
        print('meishi')


def process_one_lane(current_lane, current_inter, cars_list, signal):
    '''
    process one lane, given the signal
    '''

    current_car = cars_list
    turn = macros.STRAIGHT   # status for turning, 0: need to go straight, -1: need to turn left, 1: need to turn right
    change_lane = 0     # status for change lane, 0: don't need to change lane, 1: need to change lane

    [turn, change_lane] = check_turn_and_change_lane(current_lane, current_inter, current_car)
    if signal == macros.GREEN:
        while current_car:

            current_car = current_car.next


def check_turn_and_change_lane(current_lane, current_inter, current_car):
    '''
    process one lane, given the signal
    '''
    turn = macros.STRAIGHT   # status for turning, 0: need to go straight, -1: need to turn left, 1: need to turn right
    change_lane = 0     # status for change lane, 0: don't need to change lane, 1: need to change lane

    if current_inter == current_car.my_path[-1]:    # already at destination
        if current_lane == macros.WESTL:
            if current_car.final_dir == macros.SOUTH:
                turn = macros.RIGHT
                change_lane = 1
            elif current_car.final_dir == macros.NORTH:
                turn = macros.LEFT
                change_lane = 0
            else:
                turn = 0
                change_lane = 0
        elif current_lane == macros.WESTR:
            if current_car.final_dir == macros.SOUTH:
                turn = macros.RIGHT
                change_lane = 0
            elif current_car.final_dir == macros.NORTH:
                turn = macros.LEFT
                change_lane = 1
            else:
                turn = 0
                change_lane = 0
        elif current_lane == macros.NORTHL:
            if current_car.final_dir == macros.WEST:
                turn = macros.RIGHT
                change_lane = 1
            elif current_car.final_dir == macros.EAST:
                turn = macros.LEFT
                change_lane = 0
            else:
                turn = 0
                change_lane = 0
        elif current_lane == macros.NORTHR:
            if current_car.final_dir == macros.WEST:
                turn = macros.RIGHT
                change_lane = 0
            elif current_car.final_dir == macros.EAST:
                turn = macros.LEFT
                change_lane = 1
            else:
                turn = 0
                change_lane = 0
        elif current_lane == macros.EASTL:
            if current_car.final_dir == macros.NORTH:
                turn = macros.RIGHT
                change_lane = 1
            elif current_car.final_dir == macros.SOUTH:
                turn = macros.LEFT
                change_lane = 0
            else:
                turn = 0
                change_lane = 0
        elif current_lane == macros.EASTR:
            if current_car.final_dir == macros.NORTH:
                turn = macros.RIGHT
                change_lane = 0
            elif current_car.final_dir == macros.SOUTH:
                turn = macros.LEFT
                change_lane = 1
            else:
                turn = 0
                change_lane = 0
        elif current_lane == macros.SOUTHL:
            if current_car.final_dir == macros.EAST:
                turn = macros.RIGHT
                change_lane = 1
            elif current_car.final_dir == macros.WEST:
                turn = macros.LEFT
                change_lane = 0
            else:
                turn = 0
                change_lane = 0
        elif current_lane == macros.SOUTHR:
            if current_car.final_dir == macros.EAST:
                turn = macros.RIGHT
                change_lane = 0
            elif current_car.final_dir == macros.WEST:
                turn = macros.LEFT
                change_lane = 1
            else:
                turn = 0
                change_lane = 0

    else:
        for i in range(0, len(current_car.my_path)-1):  #decide if
            if current_inter == current_car.my_path[i]:
                next_inter = current_car.my_path[i+1]
            else:
                print("A car is not on its path!!!!!!")
                return -1

        if current_lane == macros.WESTL:
            if next_inter[0] == current_inter[0]+1:
                turn = macros.RIGHT
                change_lane = 1
            elif next_inter[0] == current_inter[0]-1:
                turn = macros.LEFT
                change_lane = 0
            elif next_inter[1] == current_inter[1]+1:
                turn = 0
                change_lane = 0
            else:
                print("You cannot make a U turn!!!!!!!")
                return -1
        elif current_lane == macros.WESTR:
            if next_inter[0] == current_inter[0]+1:
                turn = macros.RIGHT
                change_lane = 0
            elif next_inter[0] == current_inter[0]-1:
                turn = macros.LEFT
                change_lane = 1
            elif next_inter[1] == current_inter[1]+1:
                turn = 0
                change_lane = 0
            else:
                print("You cannot make a U turn!!!!!!!")
                return -1
        elif current_lane == macros.NORTHL:
            if next_inter[1] == current_inter[1]-1:
                turn = macros.RIGHT
                change_lane = 1
            elif next_inter[1] == current_inter[1]+1:
                turn = macros.LEFT
                change_lane = 0
            elif next_inter[0] == current_inter[0]+1:
                turn = 0
                change_lane = 0
            else:
                print("You cannot make a U turn!!!!!!!")
                return -1
        elif current_lane == macros.NORTHR:
            if next_inter[1] == current_inter[1]-1:
                turn = macros.RIGHT
                change_lane = 0
            elif next_inter[1] == current_inter[1]+1:
                turn = macros.LEFT
                change_lane = 1
            elif next_inter[0] == current_inter[0]+1:
                turn = 0
                change_lane = 0
            else:
                print("You cannot make a U turn!!!!!!!")
                return -1
        elif current_lane == macros.EASTL:
            if next_inter[0] == current_inter[0]+1:
                turn = macros.RIGHT
                change_lane = 1
            elif next_inter[0] == current_inter[0]-1:
                turn = macros.LEFT
                change_lane = 0
            elif next_inter[1] == current_inter[1]-1:
                turn = 0
                change_lane = 0
            else:
                print("You cannot make a U turn!!!!!!!")
                return -1
        elif current_lane == macros.EASTR:
            if next_inter[0] == current_inter[0]+1:
                turn = macros.RIGHT
                change_lane = 0
            elif next_inter[0] == current_inter[0]-1:
                turn = macros.LEFT
                change_lane = 1
            elif next_inter[1] == current_inter[1]-1:
                turn = 0
                change_lane = 0
            else:
                print("You cannot make a U turn!!!!!!!")
                return -1
        elif current_lane == macros.SOUTHL:
            if next_inter[1] == current_inter[1]+1:
                turn = macros.RIGHT
                change_lane = 1
            elif next_inter[1] == current_inter[1]-1:
                turn = macros.LEFT
                change_lane = 0
            elif next_inter[0] == current_inter[0]+1:
                turn = 0
                change_lane = 0
            else:
                print("You cannot make a U turn!!!!!!!")
                return -1
        elif current_lane == macros.SOUTHR:
            if next_inter[1] == current_inter[1]-1:
                turn = macros.RIGHT
                change_lane = 0
            elif next_inter[1] == current_inter[1]+1:
                turn = macros.LEFT
                change_lane = 1
            elif next_inter[0] == current_inter[0]+1:
                turn = 0
                change_lane = 0
            else:
                print("You cannot make a U turn!!!!!!!")
                return -1
    return [turn, change_lane]
