import map_init
import intersection_process
import car
import macros
import turtle

screen = turtle.Screen()

#car1 = car.Car(0, (1,1), macros.WEST, 10)
#
#print(car1.final_dir)
#print(car1.final_exit)
#print(car1.my_path)
#
## tested here: check_for_turn_and_change_lane()
#print(intersection_process.check_turn_and_change_lane(macros.WESTL, (1, 1), car1))


def draw_map():
    tot_width = sum(macros.HOR_DIM) + 4 * macros.LANE_WIDTH * (len(macros.HOR_DIM) - 1)
    tot_height = sum(macros.VER_DIM) + 4 * macros.LANE_WIDTH * (len(macros.VER_DIM) - 1)

    board = turtle.Turtle()
    board.pu()
    board.setposition(0, 0)

    for i in range(1, len(macros.HOR_DIM)):
        draw_ver_street(board, map_init.intersections[(1, i)].coor[0], tot_height)
    for i in range(1, len(macros.VER_DIM)):
        draw_hor_street(board, map_init.intersections[(i, 1)].coor[1], tot_width)

    screen.mainloop()


def draw_ver_street(board, pos, length):
    board.pu()
    board.setpos(pos/10, 0)
    board.seth(270)
    board.pd()
    board.forward(length/10)
    board.pu()


def draw_hor_street(board, pos, length):
    board.pu()
    board.setpos(0, pos/10)
    board.seth(0)
    board.pd()
    board.forward(length/10)
    board.pu()


map_init.map_init()
draw_map()
