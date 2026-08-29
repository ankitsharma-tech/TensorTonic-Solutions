import torch

def activate(x, method="relu"):
    """
    Returns: list (activated tensor converted via .tolist())
    """
    x = torch.tensor(x,dtype=torch.float)

    if method=="sigmoid":
        return 1/(1+torch.exp(-x))
    elif method=="relu":
        return torch.where(x>0,x,torch.zeros_like(x))
    elif method =="tanh":
        return (torch.exp(x)-torch.exp(-x))/(torch.exp(x)+torch.exp(-x))
    else:
        return torch.where(x>0,x,0.01*x)
    