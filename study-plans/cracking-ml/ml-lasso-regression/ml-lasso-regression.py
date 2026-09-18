import numpy as np

def lasso_regression(X: list, y: list, alpha: float, lr: float, epochs: int) -> tuple:
    X = np.asarray(X,float)
    y = np.asarray(y,float)
    n,d = X.shape
    w = np.zeros(d)
    b = 0
    for _ in range(epochs):
        e = ((X@w+b) - y)
        w -= lr * ((2/n) * ((X.T@e)) + (alpha * np.sign(w)))
        b -= lr * 2 * e.mean()

    return [w.tolist(),b]
