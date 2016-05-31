import map_init
import intersection_process
import car
import macros

car1 = car.Car(0, (1,1), macros.EAST, 10)

# tested here: check_for_turn_and_change_lane()
print(intersection_process.check_turn_and_change_lane(macros.WESTL, (1, 1), car1))