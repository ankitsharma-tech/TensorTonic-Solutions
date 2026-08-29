import torch

def compute_gradient(values):
    """
    Returns: list of float gradient values dy/dx
    """
    values = torch.tensor(values,requires_grad=True,dtype=torch.float)

    y = values ** 3 + 2 * values

    y.sum().backward()

    return values.grad.tolist()