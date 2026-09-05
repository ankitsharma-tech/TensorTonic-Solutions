import numpy as np

def reshape_array(data, operation):
    data = np.asarray(data,dtype="float64")
    if operation=="flatten":
        return data.flatten()
    elif operation =="transpose":
        return data.T
    elif operation == "add_batch":
        return data[None,:]