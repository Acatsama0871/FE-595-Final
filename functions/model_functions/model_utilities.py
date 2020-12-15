# model utilities.py
# the utility function for traning the model

# modules
import os
import pandas as pd

# load data function
def load_data(full=False):
    # set data path
    data_path = os.path.dirname(os.path.dirname(os.getcwd()))
    data_path = os.path.join(data_path, "Data/features.csv")

    # load data from csv
    df = pd.read_csv(data_path)

    # if load full data
    if full == False:
        del df["Date"]
        y = df.pop("direction").values
        x = df.values
    else:
        df = df[df["Date"] < "2020-01-01"]
        del df["Date"]
        y = df.pop("direction").values
        x = df.values

    return x, y
