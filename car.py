import macros


class Car:
    def __init__(self, time_tag, index, initial_ent, speed, path, location):
        self.time_tag = time_tag
        self.index = index
        self.initial_ent = initial_ent
        self.final_exit = None
        self.path = path
        self.speed = speed
        self.acc = 0
        self.wait_time = 0
        self.dist_to_front = 0
        self.next = None
        self.prev = None
        self.location = location




