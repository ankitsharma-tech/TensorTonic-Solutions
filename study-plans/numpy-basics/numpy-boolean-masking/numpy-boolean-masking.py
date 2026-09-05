import numpy as np

def row_summary(data, threshold):
    data = np.asarray(data,dtype="float64")

    mask = data > threshold

    mask_1 = mask.any(axis=1)
    data_1 = data*mask_1[:,None]

    mask_2 = mask.all(axis=1)
    data_2 = data*mask_2[:,None]

    result = mask.astype("float64")

    result = np.stack([result, data_1, data_2])

    return result