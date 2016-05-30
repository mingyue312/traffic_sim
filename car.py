import macros
import random
import path


class Car:
    def __init__(self, time_tag, initial_ent, initial_dir, speed):
        self.time_tag = time_tag
        self.initial_ent = initial_ent
        self.initial_dir = initial_dir
        self.final_exit = None
        self.final_dir = 0
        self.my_path = path.find_path(self.initial_ent, self.final_exit)
        self.speed = speed
        self.acc = 0
        self.wait_time = 0
        self.dist_to_front = 0
        self.next = None
        self.prev = None

        while True:
            self.final_exit = (random.randint(1, len(macros.VER_DIM)-1), random.randint(1, len(macros.HOR_DIM)-1))
            self.final_dir = random.randint(1,4)
            if self.final_exit != self.initial_ent:
                break




