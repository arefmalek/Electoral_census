import pandas as pd
import numpy as np
import json

with open("data_v1\Electoral_votes.json") as f:
    info = json.load(f)

df = pd.read_csv("data_v1\ACSDP1Y2010.DP05_data_with_overlays_2020-11-06T214859.csv")
df = df.drop(51)

short_names = [val["name_short"] for val in info.values()]

p = pd.DataFrame({
    "state": short_names,
    "compare": df["NAME"]
})

print(p)