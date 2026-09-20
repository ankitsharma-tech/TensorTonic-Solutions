import numpy as np

def percentiles(x: list, q: list) -> np.ndarray:
    """
    Returns the requested percentiles as a float64 array.
    """
    x = np.asarray(x,float)
    q = np.asarray(q,float)
    return np.quantile(x,q/100)