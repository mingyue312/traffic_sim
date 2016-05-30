import macros


def intersection_process(intersection, dic):
    if intersection.phase_dictionary[intersection.current_phase] > intersection.reference_dictionary[intersection.current_phase]:
        intersection.phase_dictionary[intersection.current_phase] = 0

        if intersection.current_phase + 1 > 6:
            intersection.current_phase = 0

        else:
            intersection.current_phase = intersection.current_phase + 1

