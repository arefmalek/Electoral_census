import pandas as pd

df = pd.read_csv("data_v1\ACSDP1Y2010.DP05_data_with_overlays_2020-11-06T214859.csv")
df = df.drop(0)

print(df.head())