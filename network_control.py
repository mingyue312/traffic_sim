import map_init
import random
import car
import macros

map_init.map_init()

sim_time = 0


def network_control(duration, time_increment, num_inters):
    while sim_time <= duration:
        for inter in map_init.intersections:
            for enter_lane in map_init.intersections[inter].boundary:
                if sim_time >= map_init.intersections[inter].boundary[enter_lane]: #if time to create a new car for intersection 'inter' and lane 'enter_lane'
                    new_car = car.Car(inter, macros.INITSPEED)
                    prev_arrival = map_init.intersections[inter].boundary[enter_lane]
                    map_init.intersections[inter].boundary[enter_lane] = \
                        round(random.uniform(prev_arrival, prev_arrival + macros.FREQ), 2)
