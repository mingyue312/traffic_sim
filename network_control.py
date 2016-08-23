import map_init
import random
import car_define
import macros
import intersection_process
import visualization
import qlearning_helper
#import multiagentlearning


prev_state_global = [[],[],[]]
cur_state_global = [[],[],[]]
prev_action_global = [-1,-1,-1]
n_global = [0,0,0]

def network_control():
   
    action = {}
    input_dict = {}
    for inter in map_init.intersections:
        action[inter] = 1  # start with NSGREEN_WERED
        action[inter] = -1
    prev_action = action.copy()

    while macros.SIM_TIME <= macros.DURATION:
        for inter in map_init.intersections:
            # Following block initialize cars at every intersection if needed:
            for enter_lane in map_init.intersections[inter].boundary:
            ################################### delete this block to get same car flow on all entrances.
                if macros.SIM_TIME >= map_init.intersections[inter].boundary[enter_lane] and enter_lane in [macros.WESTL, macros.WESTR]:
                    direction = macros.WEST
                    new_car = car_define.Car(inter, direction, macros.INITSPEED)
                    if not map_init.intersections[inter].cars_queue[enter_lane]:
                        map_init.intersections[inter].cars_queue[enter_lane] = new_car
                    else:
                        current_car = map_init.intersections[inter].cars_queue[enter_lane]
                        while current_car.next:
                            current_car = current_car.next
                        new_car.prev = current_car
                        current_car.next = new_car
                    prev_arrival = map_init.intersections[inter].boundary[enter_lane]
                    map_init.intersections[inter].boundary[enter_lane] = round(random.uniform(prev_arrival, prev_arrival + macros.WESTFREQ), 1)
            ####################################
                elif macros.SIM_TIME >= map_init.intersections[inter].boundary[enter_lane]: #if time to create a new car for intersection 'inter' and lane 'enter_lane'
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
                    map_init.intersections[inter].timer = round(map_init.intersections[inter].timer + macros.TIME_INCREMENT, 1)
                elif map_init.intersections[inter].current_phase in [macros.NSRED_EWGREEN, macros.NSGREEN_EWRED]:
                    if map_init.intersections[inter].timer >= macros.GREEN_PHASE:
                        map_init.intersections[inter].current_phase += 1
                        if map_init.intersections[inter].current_phase == 5:
                            map_init.intersections[inter].current_phase = 1
                        map_init.intersections[inter].timer = 0
                    map_init.intersections[inter].timer = round(map_init.intersections[inter].timer + macros.TIME_INCREMENT, 1)

            elif map_init.intersections[inter].current_phase in [macros.NSRED_EWYELLOW, macros.NSYELLOW_EWRED]:
                if map_init.intersections[inter].timer >= macros.YELLOW_PHASE:
                    map_init.intersections[inter].current_phase += 1
                    if map_init.intersections[inter].current_phase == 5:
                        map_init.intersections[inter].current_phase = 1
                    map_init.intersections[inter].timer = 0
                map_init.intersections[inter].timer = round(map_init.intersections[inter].timer + macros.TIME_INCREMENT, 1)

            elif prev_action[inter] != action[inter] and action[inter] == 1 and map_init.intersections[inter].current_phase == macros.NSRED_EWGREEN:
                map_init.intersections[inter].current_phase = macros.NSRED_EWYELLOW
                map_init.intersections[inter].timer = macros.TIME_INCREMENT
                prev_action[inter] = action[inter]
            elif prev_action[inter] != action[inter] and action[inter] == 0 and map_init.intersections[inter].current_phase == macros.NSGREEN_EWRED:
                map_init.intersections[inter].current_phase = macros.NSYELLOW_EWRED
                map_init.intersections[inter].timer = macros.TIME_INCREMENT
                prev_action[inter] = action[inter]
            else:
                map_init.intersections[inter].timer = round(map_init.intersections[inter].timer + macros.TIME_INCREMENT, 1)

            # Following block processes each intersection's car movements:
            intersection_process.intersection_process(inter)
            visualization.log_avg_car_length(inter)

        #if macros.SIM_TIME % 3 == 0:
        #    prev_action = action.copy()
        #    for inter in map_init.intersections:
        #        queue_len = qlearning_helper.get_queue_len(inter)
        #        if map_init.intersections[inter].current_phase in [macros.NSRED_EWYELLOW, macros.NSRED_EWGREEN]:
        #            queue_len += [0, map_init.intersections[inter].timer]
        #        elif map_init.intersections[inter].current_phase in [macros.NSYELLOW_EWRED, macros.NSGREEN_EWRED]:
        #            queue_len += [map_init.intersections[inter].timer, 0]
        #        input_dict[inter] = queue_len
        #        #action[inter] = random.randint(0, 1)
        #    action = multiagentlearning.qlearning(input_dict) #(prev_state_global,cur_state_global,prev_action_global,n_global)   # pass in the queue_len dictionary to qlearning and get action dictionary back

        #if macros.SIM_TIME % 100 == 0:
        #    visualization.draw_cars()
        #    visualization.draw_signal()
            #visualization.log_action_table()
            #visualization.log_q_value()

        if macros.SIM_TIME == 100:
            qlearning_helper.get_first_coherence_list()
            print(macros.prev_coherence_matrix)
        if 100 < macros.SIM_TIME < 500 and macros.SIM_TIME % 5 == 0:
            qlearning_helper.get_coherence_list()
            print(macros.prev_coherence_matrix)

        if macros.SIM_TIME == 500:
            qlearning_helper.get_coherence_list()
            print(macros.prev_coherence_matrix)

        macros.SIM_TIME = round(macros.SIM_TIME + macros.TIME_INCREMENT, 1)


map_init.map_init()
#visualization.draw_map()
visualization.log_init()
#visualization.draw_signal()
#multiagentlearning.initialize(9, 2)
network_control()
print('DONE!')