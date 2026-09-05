import numpy as np

def angle_features(angles):

    angles = np.asarray(angles,dtype="float64")

    result = np.stack([
        np.sin(angles),
        np.cos(angles),
        np.tan(angles)
    ], axis=0)
    return result