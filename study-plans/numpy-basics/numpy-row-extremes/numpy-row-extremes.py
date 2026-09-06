import numpy as np

def row_extremes(data):
    data = np.asarray(data).astype("float64")
    

    result = np.stack([
        data.max(axis=1),
        data.argmax(axis=1).astype("float64"),
        data.min(axis=1),
        data.argmin(axis=1).astype("float64")
    ],axis=0)

    return result