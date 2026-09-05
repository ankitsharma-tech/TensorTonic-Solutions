import numpy as np

def create_sequence(start, stop, param, kind):
    if kind =="arange":
        return np.arange(start,stop,param,dtype="float64")
    elif kind =="linspace":
        return np.linspace(start,stop,param,dtype="float64")
    
    
   
    