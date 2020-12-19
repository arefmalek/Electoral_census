import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statistics import mean 

income = pd.read_csv("data_v2\ACSSPP1Y2010.S0201_data_with_overlays_2020-11-14T112132.csv")
income = income.drop(0)
income = income.drop(52)


df = pd.DataFrame({
    "State": income["NAME"],
    "Median Income": income["S0201_229E"],
    "Average Earning": income["S0201_216E"]
})

print(df)

inc = [int(i) for i in df["Median Income"]]

mean_income = mean([int(i) for i in df["Average Earning"]])
lol = [mean_income] * 51


median_income = plt.plot(df["State"], inc)
avg_inc = plt.plot(df["State"], lol)

plt.legend([median_income, avg_inc], ["Median Income", "National Average"])

plt.show()