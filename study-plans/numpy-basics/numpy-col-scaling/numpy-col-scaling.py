import numpy as np

def scale_cols(data, weights):
    data = np.asarray(data,dtype="float64")
    weights = np.asarray(weights,dtype="float64")

    return data*weights