import pandas as pd

def select_column(data, column):
    df = pd.DataFrame(data)
    dict = {}

    dict["values"] = df[column].tolist()
    dict["length"] = df.shape[0]

    return dict

