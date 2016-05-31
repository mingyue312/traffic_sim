import macros

####list_of_vehicle
### add time_incre at the end of this function

def intersection_process(intersection, dic, list_of_vehicle):
    if intersection.phase_dictionary[intersection.current_phase] > intersection.reference_dictionary[intersection.current_phase]:
        intersection.phase_dictionary[intersection.current_phase] = 0

        if intersection.current_phase + 1 > 6:
            intersection.current_phase = 0

        else:
            intersection.current_phase = intersection.current_phase + 1


    if intersection.current_phase == 1 or intersection.current_phase == 4:
        
