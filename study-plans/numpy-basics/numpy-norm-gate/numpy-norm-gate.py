import numpy as np

def norm_gate(X, W, threshold):
    X = np.asarray(X,dtype="float64")
    W = np.asarray(W,dtype="float64")

    Z = X @ W 
    temp = np.linalg.norm(Z,axis=1)

    mask = temp >= threshold

    result = Z * mask[:,None]

    return result
    