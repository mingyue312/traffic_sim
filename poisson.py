import numpy as np
import macros

def poisson():
    p = np.random.poisson(macros.Number_arrival, 1)
    return p

