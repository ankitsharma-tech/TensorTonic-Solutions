import numpy as np

def kmeans(X: list, k: int, max_iters: int = 100, seed: int = 42) -> tuple:
    X = np.asarray(X,float)
    #rng = np.random.default_rng(seed)
    rng = np.random.RandomState(seed)

    centroid = X[rng.choice(len(X),k,replace=False)].copy()

    for _ in range(max_iters):
        c = centroid[None,:,:]
        x = X[:,None,:]
        dist = np.linalg.norm(x-c,axis=-1)
        lab = dist.argmin(axis=1)
        new_centroid = centroid.copy()
        for j in range(k):
            pts = X[lab==j]
            if len(pts):
                new_centroid[j] = pts.mean(axis=0)
        if np.allclose(new_centroid,centroid):
            break
        centroid = new_centroid.copy()
    cent = centroid[None,:,:]
    dist = np.linalg.norm(X[:,None,:]-cent,axis=-1)
    lab = dist.argmin(axis=1)
    return [lab,centroid.tolist()]
        
        
        
        
