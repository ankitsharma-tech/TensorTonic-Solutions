import numpy as np

def norm_diff(a, b, lo, hi):
    a = np.asarray(a, dtype="float64")
    b = np.asarray(b, dtype="float64")

    a = np.clip(a, lo, hi)
    b = np.clip(b, lo, hi)

    a = (a - lo) / (hi - lo)
    b = (b - lo) / (hi - lo)

    return np.abs(a - b)