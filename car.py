import macros
import path


class Car:
    def __init__(self, time_tag, index, initial_ent, initial_dir, speed, location):
        self.time_tag = time_tag
        self.index = index
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
        self.location = location


