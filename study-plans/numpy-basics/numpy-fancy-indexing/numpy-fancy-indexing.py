import numpy as np

def select_by_index(arr, indices, axis):
    arr = np.asarray(arr,dtype="float64")

    return np.take(arr,indices,axis=axis)
    