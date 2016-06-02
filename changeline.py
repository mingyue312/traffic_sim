import macros

def change_line(left_car_list,right_car_list, turn, car):
    ##1 means turn left
    find_lagging_car = 0
    if turn  == 1:
        current_left = left_car_list
        while current_left:
            if current_left.position < car.position:
                find_lagging_car = 1
                lagging_car = current_left
                if current_left.prev:
                    leading_car = current_left.prev
                    if (leading_car.position - lagging_car.position)/car.speed > macros.LEFT_GAP:
                        car.prev.next = car.next
                        car.next.prev = car.prev
                        car.next = lagging_car
                        lagging_car.prev = car
                        car.prev = leading_car
                        leading_car.next = car
                    else:
                        car.acc = 0.5*car.speed
                else:
                    current_left.prev = car
                    car.prev.next = car.next
                    car.next.prev = car.prev
                    car.next = current_left
                break
            if current_left.next == None:
                break
            current_left = current_left.next


        if find_lagging_car == 0:
            car.prev.next = car.next
            car.next.prev = car.prev
            car.prev = current_left


    if turn  == 2:
        current_right = right_car_list
        while current_right.next :
            if current_right.position < car.position:
                find_lagging_car = 1
                lagging_car = current_right
                if current_right.prev:
                    leading_car = current_right.prev
                    if (leading_car.position - lagging_car.position)/car.speed > macros.LEFT_GAP:
                        car.prev.next = car.next
                        car.next.prev = car.prev
                        car.next = lagging_car
                        lagging_car.prev = car
                        car.prev = leading_car
                        leading_car.next = car
                    else:
                        car.acc = 0.5*car.speed
                else:
                    current_right.prev = car
                    car.prev.next = car.next
                    car.next.prev = car.prev
                    car.next = current_right
                break
            if current_left.next == None:
                break
            current_right = current_right.next

        if find_lagging_car == 0:
            car.prev.next = car.next
            car.next.prev = car.prev
            car.prev = current_right