class car:
    def __init__(self, index, speed):
        self.index = index
        self.speed = speed
        self.acc = 0
        self.dist_to_front = 0
        self.next = None
        self.prev = None


