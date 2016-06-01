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
        self.north_green = macros.GREEN_PHASE
        self.north_red = macros.RED_PHASE
        self.current_phase = 1






