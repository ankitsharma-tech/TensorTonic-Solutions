import pandas as pd

def head_tail(data, n):
    df = pd.DataFrame(data)
    result = {}
    result["head"] = df.head(n).to_dict(orient="list")
    result["tail"] = df.tail(n).to_dict(orient="list")

    return result
    
    