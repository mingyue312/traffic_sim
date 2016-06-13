import macros
import random
import path
import map_init


class Car:
    def __init__(self, initial_ent, initial_dir, speed):
        self.initial_ent = initial_ent
        self.initial_dir = initial_dir
        self.final_exit = None
        self.final_dir = 0
        self.speed = speed
        self.acc = 0
        self.wait_time = 0
        self.dist_to_front = 0
        self.next = None
        self.prev = None
        self.position = 0
        self.turn = macros.STRAIGHT
        self.change_lane = 0

        # TODO: could make this random process faster
        while True:
            self.final_exit = (random.randint(1, len(macros.VER_DIM)-1), random.randint(1, len(macros.HOR_DIM)-1))
            self.final_dir = random.randint(1, 4)
            if map_init.is_exit(self.final_exit, self.final_dir) and \
                    (self.final_exit != self.initial_ent or self.final_dir != self.initial_dir):
                break

        self.my_path = path.find_path(self.initial_ent, self.final_exit)


def get_position(car):
    car.position = car.position + car.speed * macros.TIME_INCREMENT + 0.5 * car.acc * macros.TIME_INCREMENT ** 2


def get_speed(car):
    car.speed += car.acc * macros.TIME_INCREMENT
    if car.speed <= 0:
        car.speed = 0
        car.acc = 0
    if car.speed > 15:
        print("fuck")





