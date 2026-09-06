import numpy as np

def sort_with_indices(data, axis):
    data = np.asarray(data,dtype="float64")
    
    sorted_data = np.sort(data, axis=axis)
    sorted_indices = np.argsort(data, axis=axis).astype("float64")

    return np.stack([sorted_data, sorted_indices], axis=0)