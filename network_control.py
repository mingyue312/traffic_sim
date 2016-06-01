import map_init
import random
import car
import macros
#import intersection_process


def network_control(action):
    while macros.SIM_TIME <= macros.DURATION:
        for inter in map_init.intersections:

            # Following block initialize cars at every intersection if needed:
            for enter_lane in map_init.intersections[inter].boundary:
                if macros.SIM_TIME >= map_init.intersections[inter].boundary[enter_lane]: #if time to create a new car for intersection 'inter' and lane 'enter_lane'
                    if enter_lane in [macros.WESTL, macros.WESTR]:
                        direction = macros.WEST
                    elif enter_lane in [macros.EASTL, macros.EASTR]:
                        direction = macros.EAST
                    elif enter_lane in [macros.NORTHL, macros.NORTHR]:
                        direction = macros.NORTH
                    else:
                        direction = macros.SOUTH
                    new_car = car.Car(inter, direction, macros.INITSPEED)
                    if not map_init.intersections[inter].cars_queue[enter_lane]:
                        map_init.intersections[inter].cars_queue[enter_lane] = new_car
                    else:
                        current_car = map_init.intersections[inter].cars_queue[enter_lane]
                        while current_car.next:
                            current_car = current_car.next
                        current_car.next = new_car
                    # get next arrival time and save it to each lanes of each intersection
                    prev_arrival = map_init.intersections[inter].boundary[enter_lane]
                    map_init.intersections[inter].boundary[enter_lane] = \
                        round(random.uniform(prev_arrival, prev_arrival + macros.FREQ), 2)

            # Following block processes each intersection's car movements:
            # intersection_process.intersection_process(map_init.intersections[inter], action)

        macros.SIM_TIME += macros.TIME_INCREMENT


map_init.map_init()
network_control(1)