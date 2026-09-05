import numpy as np

def extract_subarray(arr, row_start, row_stop, col_start, col_stop):
    arr = np.asarray(arr,dtype="float64")

    return arr[row_start:row_stop,col_start:col_stop]
    
