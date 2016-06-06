import map_init
import intersection_process
import car
import macros
import turtle

screen = turtle.Screen()

car1 = car.Car(0, (1,1), macros.WEST, 10)

print(car1.final_dir)
print(car1.final_exit)
print(car1.my_path)

# tested here: check_for_turn_and_change_lane()
print(intersection_process.check_turn_and_change_lane(macros.WESTL, (1, 1), car1))

