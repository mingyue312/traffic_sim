import macros

phase_dictionary = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}


class Intersection:
    def __init__(self, name, north_len, south_len, west_len, east_len, phase_dictionary):
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
        self.phase_dictionary = phase_dictionary
        self.reference_dictionary = {1: self.north_green, 2: macros.YELLOW_PHASE, 3: macros.CLEAR_PHASE,
                                     4: self.north_red, 5: macros.YELLOW_PHASE, 6: macros.CLEAR_PHASE}





