import map_init
import macros
import turtle
import qlearning_helper
import datetime

screen = turtle.Screen()
screen.setworldcoordinates(0, -1100, 1400, 0)
board = turtle.Turtle()
board.ht()
board.speed(0)
board.pu()
board.setposition(0, 0)
car_dot = turtle.Turtle()
car_dot.ht()
car_dot.speed(0)
signal = turtle.Turtle()
signal.ht()
signal.speed(0)


def draw_map():
    tot_width = (sum(macros.HOR_DIM) + 4 * macros.LANE_WIDTH * (len(macros.HOR_DIM) - 1))
    tot_height = (sum(macros.VER_DIM) + 4 * macros.LANE_WIDTH * (len(macros.VER_DIM) - 1))
    for i in range(1, len(macros.HOR_DIM)):
        draw_ver_street((map_init.intersections[(1, i)].coor[0]) * macros.SCALE, tot_height * macros.SCALE)
    for i in range(1, len(macros.VER_DIM)):
        draw_hor_street((map_init.intersections[(i, 1)].coor[1]) * macros.SCALE, tot_width * macros.SCALE)
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
            car_dot.setpos((interx - 6 - wl + current_car.position) * macros.SCALE, (intery - 1.5) * macros.SCALE)
            car_dot.dot(1.5 * macros.SCALE, "red")
            current_car = current_car.next

        current_car = map_init.intersections[inter].cars_queue[macros.WESTR]
        while current_car:
            car_dot.setpos((interx - 6 - wl + current_car.position) * macros.SCALE, (intery - 4.5) * macros.SCALE)
            car_dot.dot(1.5 * macros.SCALE, "red")
            current_car = current_car.next

        current_car = map_init.intersections[inter].cars_queue[macros.EASTL]
        while current_car:
            car_dot.setpos((interx + 6 + el - current_car.position) * macros.SCALE, (intery + 1.5) * macros.SCALE)
            car_dot.dot(1.5 * macros.SCALE, "red")
            current_car = current_car.next

        current_car = map_init.intersections[inter].cars_queue[macros.EASTR]
        while current_car:
            car_dot.setpos((interx + 6 + el - current_car.position) * macros.SCALE, (intery + 4.5) * macros.SCALE)
            car_dot.dot(1.5 * macros.SCALE, "red")
            current_car = current_car.next

        current_car = map_init.intersections[inter].cars_queue[macros.NORTHL]
        while current_car:
            car_dot.setpos((interx - 1.5) * macros.SCALE, (intery + 6 + nl - current_car.position) * macros.SCALE)
            car_dot.dot(1.5 * macros.SCALE, "red")
            current_car = current_car.next

        current_car = map_init.intersections[inter].cars_queue[macros.NORTHR]
        while current_car:
            car_dot.setpos((interx - 4.5) * macros.SCALE, (intery + 6 + nl - current_car.position) * macros.SCALE)
            car_dot.dot(1.5 * macros.SCALE, "red")
            current_car = current_car.next

        current_car = map_init.intersections[inter].cars_queue[macros.SOUTHL]
        while current_car:
            car_dot.setpos((interx + 1.5) * macros.SCALE, (intery - 6 - sl + current_car.position) * macros.SCALE)
            car_dot.dot(1.5 * macros.SCALE, "red")
            current_car = current_car.next

        current_car = map_init.intersections[inter].cars_queue[macros.SOUTHR]
        while current_car:
            car_dot.setpos((interx + 4.5) * macros.SCALE, (intery - 6 - sl + current_car.position) * macros.SCALE)
            car_dot.dot(1.5 * macros.SCALE, "red")
            current_car = current_car.next
    car_dot.pu()
    return


def draw_signal():
    signal.clear()
    signal.pu()
    for inter in map_init.intersections:
        if map_init.intersections[inter].current_phase == macros.NSGREEN_EWRED:
            signal.setpos((map_init.intersections[inter].coor[0] - 10) * macros.SCALE, (map_init.intersections[inter].coor[1] + 14) * macros.SCALE )
            signal.dot(5, "green")
            signal.setpos((map_init.intersections[inter].coor[0] + 10) * macros.SCALE, (map_init.intersections[inter].coor[1] - 14) * macros.SCALE)
            signal.dot(5, "green")
            signal.setpos((map_init.intersections[inter].coor[0] - 14) * macros.SCALE, (map_init.intersections[inter].coor[1] - 10) * macros.SCALE)
            signal.dot(5, "red")
            signal.setpos((map_init.intersections[inter].coor[0] + 14) * macros.SCALE, (map_init.intersections[inter].coor[1] + 10) * macros.SCALE)
            signal.dot(5, "red")
        elif map_init.intersections[inter].current_phase == macros.NSYELLOW_EWRED:
            signal.setpos((map_init.intersections[inter].coor[0] - 10) * macros.SCALE, (map_init.intersections[inter].coor[1] + 14) * macros.SCALE )
            signal.dot(5, "yellow")
            signal.setpos((map_init.intersections[inter].coor[0] + 10) * macros.SCALE, (map_init.intersections[inter].coor[1] - 14) * macros.SCALE)
            signal.dot(5, "yellow")
            signal.setpos((map_init.intersections[inter].coor[0] - 14) * macros.SCALE, (map_init.intersections[inter].coor[1] - 10) * macros.SCALE)
            signal.dot(5, "red")
            signal.setpos((map_init.intersections[inter].coor[0] + 14) * macros.SCALE, (map_init.intersections[inter].coor[1] + 10) * macros.SCALE)
            signal.dot(5, "red")
        elif map_init.intersections[inter].current_phase == macros.NSRED_EWGREEN:
            signal.setpos((map_init.intersections[inter].coor[0] - 10) * macros.SCALE, (map_init.intersections[inter].coor[1] + 14) * macros.SCALE )
            signal.dot(5, "red")
            signal.setpos((map_init.intersections[inter].coor[0] + 10) * macros.SCALE, (map_init.intersections[inter].coor[1] - 14) * macros.SCALE)
            signal.dot(5, "red")
            signal.setpos((map_init.intersections[inter].coor[0] - 14) * macros.SCALE, (map_init.intersections[inter].coor[1] - 10) * macros.SCALE)
            signal.dot(5, "green")
            signal.setpos((map_init.intersections[inter].coor[0] + 14) * macros.SCALE, (map_init.intersections[inter].coor[1] + 10) * macros.SCALE)
            signal.dot(5, "green")
        elif map_init.intersections[inter].current_phase == macros.NSRED_EWYELLOW:
            signal.setpos((map_init.intersections[inter].coor[0] - 10) * macros.SCALE, (map_init.intersections[inter].coor[1] + 14) * macros.SCALE )
            signal.dot(5, "red")
            signal.setpos((map_init.intersections[inter].coor[0] + 10) * macros.SCALE, (map_init.intersections[inter].coor[1] - 14) * macros.SCALE)
            signal.dot(5, "red")
            signal.setpos((map_init.intersections[inter].coor[0] - 14) * macros.SCALE, (map_init.intersections[inter].coor[1] - 10) * macros.SCALE)
            signal.dot(5, "yellow")
            signal.setpos((map_init.intersections[inter].coor[0] + 14) * macros.SCALE, (map_init.intersections[inter].coor[1] + 10) * macros.SCALE)
            signal.dot(5, "yellow")
    signal.pu()
    return


def draw_ver_street(pos, length):
    board.setpos(pos, 0)
    board.seth(270)
    board.pd()
    board.forward(length)
    board.pu()

    board.setpos(pos + 6 * macros.SCALE, 0)
    board.seth(270)
    board.pd()
    board.forward(length)
    board.pu()

    board.setpos(pos - 6 * macros.SCALE, 0)
    board.seth(270)
    board.pd()
    board.forward(length)
    board.pu()

    board.setpos(pos + 3 * macros.SCALE, 0)
    board.seth(270)
    sign = 1
    while board.ycor() > (-length):
        if sign == 1:
            board.pd()
        board.forward(10)
        board.pu()
        sign *= -1

    board.setpos(pos - 3 * macros.SCALE, 0)
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

    board.setpos(0, pos + 6 * macros.SCALE)
    board.seth(0)
    board.pd()
    board.forward(length)
    board.pu()

    board.setpos(0, pos - 6 * macros.SCALE)
    board.seth(0)
    board.pd()
    board.forward(length)
    board.pu()

    board.setpos(0, pos + 3 * macros.SCALE)
    board.seth(0)
    sign = 1
    while board.xcor() < (length-1):
        if sign == 1:
            board.pd()
        board.forward(10)
        board.pu()
        sign *= -1

    board.setpos(0, pos - 3 * macros.SCALE)
    board.seth(0)
    sign = 1
    while board.xcor() < (length-1):
        if sign == 1:
            board.pd()
        board.forward(10)
        board.pu()
        sign *= -1


def log_init():
    f = open('./avg_queue_length_log.txt', 'a')
    #f.seek(0, 2)
    f.write('\n\n' + str(datetime.datetime.now()) + ':')
    f.write('\nSIM_TIME INTERSECTION: AVG_LENGTH')


def log_avg_car_length(internum):
    inter = map_init.intersections[internum]
    length = qlearning_helper.get_queue_len(internum)
    avg_len = sum(length)/8
    inter_name = str(internum)
    time = str(macros.SIM_TIME)
    f = open('./avg_queue_length_log.txt', 'a')
    #f.seek(0, 2)
    f.write('\n' + time + '\t'+ inter_name + ':\t' + str(avg_len))

#map_init.map_init()
#draw_map()
#map_init.intersections[(1,1)].current_phase = 2
#draw_signa#l()

log_init()
