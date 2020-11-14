import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json

df = pd.read_csv("data_v1\ACSDP1Y2010.DP05_data_with_overlays_2020-11-06T214859.csv")
df = df.drop(51)

# print(df["Geographic Area Name"], df["Estimate Margin of Error!!RACE!!One race!!Native Hawaiian and Other Pacific Islander!!Native Hawaiian"])
# print(df.head())

with open("data_v1\Electoral_votes.json") as f:
    info = json.load(f)

short_names = [val["name_short"] for val in info.values()]

race = pd.DataFrame({
    "State": short_names,
    "White": df["DP05_0032PE"],
    "Black": df["DP05_0033PE"],
    "Asian": df["DP05_0039PE"],
    "Latino": df["DP05_0066PE"],
    "Native American": df["DP05_0035PE"],
    "Pacific Islander": df["DP05_0047PE"]
})

race["Native American"] = race["Native American"].replace("[N]", "0.0",regex=True)

print(race)
ind = race["State"]    # the x locations for the groups
width = .8      # the width of the bars: can also be len(x) sequence
percentages = [race["Black"], 
race["Asian"], race["Latino"],
race["Pacific Islander"], race["Native American"]]


filler = plt.bar(
    ind, np.full((51), 100, dtype=np.int32), 
    width, color="lime"
)

white = plt.bar(
    ind, race["White"], width,
             bottom= 100 - race["White"], color="blue")


black = plt.bar(
    ind, race["Black"], width, color="orange"
)
asian = plt.bar(
    ind,percentages[1], width, 
    bottom=sum(percentages[:1]), color="yellow"
)
latino = plt.bar(
    ind, percentages[2], width,
    bottom=sum(percentages[:2]), color="brown"
)
islander = plt.bar(
    ind, percentages[3], width, 
    bottom=sum(percentages[:3]), color="green"
)

native = plt.bar(
    ind, percentages[4], width,
    bottom=sum(percentages[:4]), color="pink"
)


plt.ylabel('Percentage Makeup')
plt.title('Percentage Breakdown of Race')

plt.legend(
    [black, asian, latino, islander, native, white, filler], 
    ["Black", "Asian", "Latino", "Islander", "Native", "White", "Other"] )
plt.yticks(np.arange(0, 101, 10), range(0, 105, 10)) 
plt.xticks(race["State"], rotation=90)

plt.show()