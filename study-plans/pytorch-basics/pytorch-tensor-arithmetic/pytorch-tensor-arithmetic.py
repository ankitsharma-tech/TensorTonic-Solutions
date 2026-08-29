import torch

def tensor_op(x, y, op):
    """
    Returns: list (result tensor converted via .tolist())
    """
    x = torch.tensor(x)
    y = torch.tensor(y)
    if op == "add":
        return (x+y).tolist()
    elif op=="multiply":
        return (x*y).tolist()
    elif op=="matmul":
        return (x@y).tolist()
    elif op=="power":
        return (x**y).tolist()
    elif op=="max":
        return torch.max(x,y)
    else:
        return None