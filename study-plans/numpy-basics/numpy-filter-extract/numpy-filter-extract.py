import numpy as np

def filter_and_extract(data, row_start, row_stop, threshold):
    data = np.asarray(data,dtype="float64")

    data = data[row_start:row_stop,:]

    return data [data>threshold]
    