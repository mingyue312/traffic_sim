import map_init
import random
import car_define
import macros
import intersection_process
import visualization
import qlearning_helper
#import Qlearning4


def network_control():
    action = {}
    input_dict = {}
    for inter in map_init.intersections:
        #action[inter] = 1  # start with NSGREEN_WERED
        action[inter] = -1
    prev_action = action

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
                    new_car = car_define.Car(inter, direction, macros.INITSPEED)
                    if not map_init.intersections[inter].cars_queue[enter_lane]:
                        map_init.intersections[inter].cars_queue[enter_lane] = new_car
                    else:
                        current_car = map_init.intersections[inter].cars_queue[enter_lane]
                        while current_car.next:
                            current_car = current_car.next
                        new_car.prev = current_car
                        current_car.next = new_car
                    # get next arrival time and save it to each lanes of each intersection
                    prev_arrival = map_init.intersections[inter].boundary[enter_lane]
                    map_init.intersections[inter].boundary[enter_lane] = \
                        round(random.uniform(prev_arrival, prev_arrival + macros.FREQ), 1)

            # this variable controls the phase of each intersection.
            # -1: autonomous phase control, 1: change phase, 0: keep current phase
            # if not autonomous, this signal should be produced by learning algorithm

            if action[inter] == -1:
                if map_init.intersections[inter].current_phase in [macros.NSRED_EWYELLOW, macros.NSYELLOW_EWRED]:
                    if map_init.intersections[inter].timer >= macros.YELLOW_PHASE:
                        map_init.intersections[inter].current_phase += 1
                        if map_init.intersections[inter].current_phase == 5:
                            map_init.intersections[inter].current_phase = 1
                        map_init.intersections[inter].timer = 0
                        visualization.draw_signal()
                    map_init.intersections[inter].timer = round(map_init.intersections[inter].timer + macros.TIME_INCREMENT, 1)
                elif map_init.intersections[inter].current_phase in [macros.NSRED_EWGREEN, macros.NSGREEN_EWRED]:
                    if map_init.intersections[inter].timer >= macros.GREEN_PHASE:
                        map_init.intersections[inter].current_phase += 1
                        if map_init.intersections[inter].current_phase == 5:
                            map_init.intersections[inter].current_phase = 1
                        map_init.intersections[inter].timer = 0
                        visualization.draw_signal()
                    map_init.intersections[inter].timer = round(map_init.intersections[inter].timer + macros.TIME_INCREMENT, 1)

            elif map_init.intersections[inter].current_phase in [macros.NSRED_EWYELLOW, macros.NSYELLOW_EWRED]:
                if map_init.intersections[inter].timer >= macros.YELLOW_PHASE:
                    map_init.intersections[inter].current_phase += 1
                    if map_init.intersections[inter].current_phase == 5:
                        map_init.intersections[inter].current_phase = 1
                    map_init.intersections[inter].timer = 0
                    visualization.draw_signal()
                map_init.intersections[inter].timer = round(map_init.intersections[inter].timer + macros.TIME_INCREMENT, 1)

            elif prev_action[inter] != action[inter] and action[inter] == 1 and map_init.intersections[inter].current_phase == macros.NSRED_EWGREEN:
                map_init.intersections[inter].current_phase = macros.NSRED_EWYELLOW
                map_init.intersections[inter].timer = macros.TIME_INCREMENT
                visualization.draw_signal()
                prev_action = action
            elif prev_action[inter] != action[inter] and action[inter] == 0 and map_init.intersections[inter].current_phase == macros.NSGREEN_EWRED:
                map_init.intersections[inter].current_phase = macros.NSYELLOW_EWRED
                map_init.intersections[inter].timer = macros.TIME_INCREMENT
                visualization.draw_signal()
                prev_action = action
            else:
                map_init.intersections[inter].timer = round(map_init.intersections[inter].timer + macros.TIME_INCREMENT, 1)

            # Following block processes each intersection's car movements:
            intersection_process.intersection_process(inter)
            visualization.log_avg_car_length(inter)

        if macros.SIM_TIME % 3 == 0:
            for inter in map_init.intersections:
                queue_len = qlearning_helper.get_queue_len(inter)
                queue_len.append(map_init.intersections[inter].timer)
                input_dict[inter] = queue_len
            prev_action = action
            #action = Qlearning4.qlearning(input_dict)
        if macros.SIM_TIME % 50 == 0:
            visualization.draw_cars()

        macros.SIM_TIME = round(macros.SIM_TIME + macros.TIME_INCREMENT, 1)


map_init.map_init()
visualization.draw_map()
visualization.log_init()
visualization.draw_signal()
network_control()
