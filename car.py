import macros


class Car:
    def __init__(self, index, speed, path):
        self.index = index
        self.path = path
        self.speed = speed
        self.acc = 0
        self.wait_time = 0
        self.dist_to_front = 0
        self.next = None
        self.prev = None


