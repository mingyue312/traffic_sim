import map_init
import intersection_process
import car
import macros
import turtle

map_init.map_init()
#car1 = car.Car(0, (1,1), macros.WEST, 10)
#
#print(car1.final_dir)
#print(car1.final_exit)
#print(car1.my_path)
#
## tested here: check_for_turn_and_change_lane()
#print(intersection_process.check_turn_and_change_lane(macros.WESTL, (1, 1), car1))

tot_width = sum(macros.HOR_DIM) + 4 * macros.LANE_WIDTH * (len(macros.HOR_DIM) - 1)
tot_height = sum(macros.VER_DIM) + 4 * macros.LANE_WIDTH * (len(macros.VER_DIM) - 1)

wn = turtle.Screen()
MAP = turtle.Turtle()
MAP.setposition(0, 0)
MAP.pd()

for i in range(1, len)

MAP.setpos(0, 0)

wn.mainloop()


def draw_street(board, pos, direction, length):
    board.seth()
