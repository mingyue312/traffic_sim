import macros
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

def process_one_lane(cars_list):
    current_car = cars_list
    while current_car:
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

            current_car = current_car.next

class car:
    def __init__(self, position,speed):
        self.next = None
        self.prev = None
        self.speed = speed
        self.location = position


car1 = car(5,7)
car2 = car(13,7)
car3 = car(27,7)
car4 = car(33,7)

car1.next = car2
car2.prev = car1
car2.next = car3
car3.prev = car2
car3.next = car4
car4.prev = car3

car5 = car(8,7)
car6 = car(14,7)
car7 = car(23,7)
car8 = car(35,7)

car5.next = car6
car6.prev = car5
car6.next = car7
car7.prev = car6
car7.next = car8
car8.prev = car7

process_one_lane(car1)



