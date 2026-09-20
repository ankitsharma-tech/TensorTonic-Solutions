import numpy as np
from scipy import stats

def mean_median_mode(x: list) -> dict:
    x = np.asarray(x,float)
    dict = {
        "mean" : np.mean(x),
        "median" : np.median(x),
        "mode" : stats.mode(x)[0]
    }

    return dict