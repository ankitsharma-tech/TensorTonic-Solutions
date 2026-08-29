import torch

def reshape_tensor(x, op):
    """
    Returns: list
    """
    x = torch.tensor(x,dtype=torch.float)
    if op=="flatten":
        return x.flatten().tolist()
    elif op=="squeeze":
        return x.squeeze().tolist()
    elif op=="unsqueeze":
        return x.unsqueeze().tolist()
    elif op=="transpose":
        return x.T.tolist()
    else:
        return None
