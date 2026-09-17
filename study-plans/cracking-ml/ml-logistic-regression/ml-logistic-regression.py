import numpy as np

def logistic_regression(X: list, y: list, lr: float, n_iters: int) -> tuple:
    X = np.asarray(X,float)
    y = np.asarray(y,float)
    n,d = X.shape
    w = np.zeros(d)
    b = 0

    def stable_sigmoid(x):
        x = np.asarray(x,float)
        out = np.empty_like(x)
        pos = x>=0
        out[pos] = 1/(1+np.exp(-x[pos]))
        e = np.exp(x[~pos])
        out[~pos]= e/(1+e)
        return out
    for _ in range(n_iters):
        p = stable_sigmoid(X@w+b)
        e = p-y
        w -= lr * ((X.T @ e)/n)
        b -= lr * e.mean()
    return [w.tolist(),b]
        
