import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data_v1\ACSDP1Y2010.DP05_data_with_overlays_2020-11-06T214859.csv")

# print(df["Geographic Area Name"], df["Estimate Margin of Error!!RACE!!One race!!Native Hawaiian and Other Pacific Islander!!Native Hawaiian"])
# print(df.head())

race = pd.DataFrame({
    "State": df["NAME"],
    "White": df["DP05_0032PE"],
    "Black": df["DP05_0033PE"],
    "Asian": df["DP05_0039PE"],
    "Latino": df["DP05_0066PE"],
    "Native American": df["DP05_0035PE"]
})




ind = race["State"]    # the x locations for the groups
width = .8      # the width of the bars: can also be len(x) sequence
percentages = [race["Black"], race["Asian"], race["Latino"], race["Native American"]]


black = plt.bar(
    ind, race["Black"], width, color="orange"
)
asian = plt.bar(
    ind,percentages[1], width, 
    bottom=sum(percentages[:1]), color="yellow"
)
latino = plt.bar(
    ind, percentages[2], width,
    bottom=sum(percentages[:2]), color="brown")
native = plt.bar(
    ind, percentages[3], width,
    bottom=sum(percentages[:3]), color="red"
)



white = plt.bar(
    ind, race["White"], width,
             bottom= 100 - race["White"], color="blue")

plt.ylabel('State')
plt.title('Percentage Breakdown of Race')

plt.yticks(np.arange(0, 110, 10))
plt.legend(('Black', "Asian", "Latino", "native",'White'))

plt.show()