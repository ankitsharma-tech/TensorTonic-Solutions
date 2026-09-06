import numpy as np

def summarize(data, axis):
    data = np.asarray(data,dtype="float64")

    result = np.stack([
        data.mean(axis=axis),
        data.std(axis=axis),
        data.min(axis=axis),
        data.max(axis=axis)
    ],axis=0)

    return result
    
    