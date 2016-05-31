import macros

def change_line(left_car_list,right_car_list, turn, car):
    ##1 means turn left
    if turn  == 1:
        current_left = left_car_list
        while current_left :
            if current_left.position < car.position:
                lagging_car = current_left
                leading_car = current_left.prev
                break
            current_left = current_left.next

        if (leading_car.position - lagging_car.position)/car.speed > macros.l_change_gap:
            