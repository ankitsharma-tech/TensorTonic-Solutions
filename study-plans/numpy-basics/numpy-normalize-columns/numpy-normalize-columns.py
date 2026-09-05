import numpy as np

def normalize(data):
    data = np.asarray(data,dtype="float64")

    mean = data.mean(axis=0)
    std = data.std(axis=0)

    return (data-mean)/std
    