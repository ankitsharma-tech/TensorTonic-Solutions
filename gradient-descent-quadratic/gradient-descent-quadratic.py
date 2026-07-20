import torch
def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    x = torch.tensor(float(x0),requires_grad = True)
    
    for _ in range(steps):
        y = a* x**2+b*x+c
        y.backward()
        with torch.no_grad():
            x-= lr * x.grad
        x.grad.zero_()

        

    return x.item()