import numpy as np

def original_and_clipped(data, row_idx, lo, hi):
    data = np.asarray(data,dtype="float64")

    row_1 = data[row_idx,:]

    row_2 = row_1.clip(lo,hi)

    result = np.array(row_1)

    return np.stack([result,row_2])