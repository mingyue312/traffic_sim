import map_init
import macros
import turtle

screen = turtle.Screen()
screen.setworldcoordinates(-100, -800, 800, 100)
board = turtle.Turtle()
board.ht()
board.pu()
board.setposition(0, 0)
board.speed(0)
car_dot = turtle.Turtle()
car_dot.ht()


def draw_map():
    tot_width = sum(macros.HOR_DIM) + 4 * macros.LANE_WIDTH * (len(macros.HOR_DIM) - 1)
    tot_height = sum(macros.VER_DIM) + 4 * macros.LANE_WIDTH * (len(macros.VER_DIM) - 1)
    for i in range(1, len(macros.HOR_DIM)):
        draw_ver_street(map_init.intersections[(1, i)].coor[0], tot_height)
    for i in range(1, len(macros.VER_DIM)):
        draw_hor_street(map_init.intersections[(i, 1)].coor[1], tot_width)
    return


def draw_cars():
    car_dot.clear()
    car_dot.pu()
    for inter in map_init.intersections:
        interx = map_init.intersections[inter].coor[0]
        intery = map_init.intersections[inter].coor[1]
        wl = map_init.intersections[inter].west_len
        el = map_init.intersections[inter].east_len
        nl = map_init.intersections[inter].north_len
        sl = map_init.intersections[inter].south_len
        # draw cars from each of the 8 lanes
        current_car = map_init.intersections[inter].cars_queue[macros.WESTL]
        while current_car:
            car_dot.setpos(interx - 6 - wl + current_car.location, intery - 1.5)
            car_dot.dot(2, "red")
            current_car = current_car.next

        current_car = map_init.intersections[inter].cars_queue[macros.WESTR]
        while current_car:
            car_dot.setpos(interx - 6 - wl + current_car.location, intery - 4.5)
            car_dot.dot(2, "red")
            current_car = current_car.next

        current_car = map_init.intersections[inter].cars_queue[macros.EASTL]
        while current_car:
            car_dot.setpos(interx + 6 + el - current_car.location, intery + 1.5)
            car_dot.dot(2, "red")
            current_car = current_car.next

        current_car = map_init.intersections[inter].cars_queue[macros.EASTR]
        while current_car:
            car_dot.setpos(interx + 6 + el - current_car.location, intery + 4.5)
            car_dot.dot(2, "red")
            current_car = current_car.next

        current_car = map_init.intersections[inter].cars_queue[macros.NORTHL]
        while current_car:
            car_dot.setpos(interx - 1.5, intery + 6 + nl - current_car.location)
            car_dot.dot(2, "red")
            current_car = current_car.next

        current_car = map_init.intersections[inter].cars_queue[macros.NORTHR]
        while current_car:
            car_dot.setpos(interx - 4.5, intery + 6 + nl - current_car.location)
            car_dot.dot(2, "red")
            current_car = current_car.next

        current_car = map_init.intersections[inter].cars_queue[macros.SOUTHL]
        while current_car:
            car_dot.setpos(interx + 1.5, intery - 6 - sl + current_car.location)
            car_dot.dot(2, "red")
            current_car = current_car.next

        current_car = map_init.intersections[inter].cars_queue[macros.SOUTHR]
        while current_car:
            car_dot.setpos(interx + 4.5, intery - 6 - sl + current_car.location)
            car_dot.dot(2, "red")
            current_car = current_car.next

    board.pu()
    return


def draw_ver_street(pos, length):
    board.setpos(pos, 0)
    board.seth(270)
    board.pd()
    board.forward(length)
    board.pu()

    board.setpos(pos + 6, 0)
    board.seth(270)
    board.pd()
    board.forward(length)
    board.pu()

    board.setpos(pos - 6, 0)
    board.seth(270)
    board.pd()
    board.forward(length)
    board.pu()

    board.setpos(pos + 3, 0)
    board.seth(270)
    sign = 1
    while board.ycor() > (-length):
        if sign == 1:
            board.pd()
        board.forward(10)
        board.pu()
        sign *= -1

    board.setpos(pos - 3, 0)
    board.seth(270)
    sign = 1
    while board.ycor() > (-length):
        if sign == 1:
            board.pd()
        board.forward(10)
        board.pu()
        sign *= -1


def draw_hor_street(pos, length):
    board.setpos(0, pos)
    board.seth(0)
    board.pd()
    board.forward(length)
    board.pu()

    board.setpos(0, pos + 6)
    board.seth(0)
    board.pd()
    board.forward(length)
    board.pu()

    board.setpos(0, pos - 6)
    board.seth(0)
    board.pd()
    board.forward(length)
    board.pu()

    board.setpos(0, pos + 3)
    board.seth(0)
    sign = 1
    while board.xcor() < (length-1):
        if sign == 1:
            board.pd()
        board.forward(10)
        board.pu()
        sign *= -1

    board.setpos(0, pos - 3)
    board.seth(0)
    sign = 1
    while board.xcor() < (length-1):
        if sign == 1:
            board.pd()
        board.forward(10)
        board.pu()
        sign *= -1


#map_init.map_init()
#draw_map()
#screen.mainloop()
