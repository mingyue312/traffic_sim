import map_init
import car
import macros

map_init.map_init()

sim_time = 0


def network_control(duration, time_increment, num_inters):
    while sim_time <= duration:
        for inter in map_init.intersections:
            for enter_lane in map_init.intersections[inter].boundary:
                if sim_time >= map_init.intersections[inter].boundary[enter_lane][0]:
                    new_car = car.Car(sim_time, )
                    map_init.intersections[inter].
