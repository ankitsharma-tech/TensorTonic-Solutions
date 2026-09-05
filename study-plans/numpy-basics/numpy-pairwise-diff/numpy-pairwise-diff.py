import numpy as np

def pairwise_diff(a):
    a = np.asarray(a,dtype="float64")
    return a[:,None]-a[None,:]