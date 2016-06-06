class Intersection:
    def __init__(self, north_len):
        self.north_len = north_len

inter = Intersection(10)

a = "north_len"

print (getattr(inter,a))

