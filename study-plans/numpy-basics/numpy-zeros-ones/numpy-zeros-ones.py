import numpy as np

def create_filled_array(shape, kind):
    if kind=="zeros":
        return np.zeros(shape)
    elif kind =="ones":
        return np.ones(shape)
