import numpy as np
import math

def sample_var_std(x: list) -> dict:
    """
    Returns sample variance and standard deviation as Python floats.
    """
    x = np.asarray(x,float)
    variance = sum((x-np.mean(x))**2)/(len(x)-1)
    
    dict = {
        "variance" : variance,
        "std_dev" :  np.pow(variance,0.5)
    }
    return dict