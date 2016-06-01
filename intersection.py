import macros



class Intersection:
    def __init__(self, name, north_len, south_len, west_len, east_len):
        self.name = name
        self.north_len = north_len
        self.south_len = south_len
        self.west_len = west_len
        self.east_len = east_len
        self.car_from_nl = None
        self.car_from_sl = None
        self.car_from_wl = None
        self.car_from_el = None
        self.car_from_nr = None
        self.car_from_sr = None
        self.car_from_wr = None
        self.car_from_er = None
        self.north = None
        self.south = None
        self.west = None
        self.east = None
        self.boundary = {}  #example: boundary(1)=[arrival, next arrival]   means intersection has boundary from west with arrival time and next arrival time
        self.north_green = macros.GREEN_PHASE
        self.north_red = macros.RED_PHASE
        self.current_phase = 1






