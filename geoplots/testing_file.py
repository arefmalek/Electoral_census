import pandas as pd
import numpy as np
import matplotlib
import seaborn as sns

data = pd.read_csv("aref\Data\\2019_full.csv")
data["Hawaii!!Percent"] = data["Hawaii!!Percent"].str.rstrip("%")
data = data.dropna()

data = data.drop(data.index[data["Hawaii!!Percent"].str.contains("^\D")])
data = data.drop(data.index[data["Hawaii!!Percent"].str.contains(",")])

data["Expected"] = data["Hawaii!!Percent"].astype(float) * 538 / 100
print(data)
# data.to_csv("aref/Data/2019Expected", index=False)