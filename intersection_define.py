import macros


class Intersection:
    def __init__(self, name, north_len, south_len, west_len, east_len):
        self.name = name
        self.north_len = north_len
        self.south_len = south_len
        self.west_len = west_len
        self.east_len = east_len
        self.cars_queue = {macros.WESTL: None, macros.WESTR: None, macros.EASTL: None, macros.EASTR: None,
                           macros.NORTHL: None, macros.NORTHR: None, macros.SOUTHL: None, macros.SOUTHR: None}
        self.north = None
        self.south = None
        self.west = None
        self.east = None
        self.boundary = {}  #example: boundary(1)=[arrival, next arrival]   means intersection has boundary from west with arrival time and next arrival time
        self.current_phase = 1
        self.action = 0
        self.yellow = 2
        self.count_yellow = 0
        self.coor = ()
        self.timer = 0.0  # timer keeps track of the time elapsed for current phase

    def append(self, lane, target):
        current = self.cars_queue[lane]
        if current:
            while current.next != None:
                current = current.next
            current.next = target
        else:
            self.cars_queue[lane] = target



