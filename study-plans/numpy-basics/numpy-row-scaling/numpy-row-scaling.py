import numpy as np

def scale_rows(data, weights):
    data = np.asarray(data,dtype="float64")
    weights = np.asarray(weights,dtype="float64")

    return data*weights[:,None]