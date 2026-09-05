import numpy as np

def outer_sum(a, b):

    a = np.asarray(a,dtype="float64")
    b = np.asarray(b,dtype="float64")
    return a[:,None]+b[None,:]