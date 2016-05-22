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

    def set_neighbors(self, north, south, west, east):
        self.north = north
        self.south = south
        self.west = west
        self.east = east

