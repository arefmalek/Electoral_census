import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import geoplot

us = gpd.read_file("gplot_files\cb_2018_us_state_20m.shp")

# grad_df = pd.read_csv("aref\Data\ACSDT1Y2019.B15002A_data_with_overlays_2020-11-14T232802.csv")

# print(grad_df["B15002A_005E"])
# us["male_hs"] = grad_df["B15002A_005E"]
# us["female_hs"] = grad_df["B15002A_014E"]

# print(grad_df["latino_hs_graduate"])

density_df = pd.read_csv("aref\Data\density.csv")

ecv_df = pd.read_csv("aref\Data\state_data")

# us.plot(column='male_hs', ax=ax, cmap='Greens')
# us.plot(column="female_hs", ax=ax, cmap="Reds")

us["density"] = density_df["Density per square mile of land area"]
us.loc[us["density"] >= 500, "density"] = 500

us["Electoral"] = (ecv_df["E.C. Votes"] / ecv_df["Population"]) * 1_000_000


f, ax = plt.subplots(1, figsize=(100, 100))


# us.plot(
#     column="density", ax=ax,
#     cmap="Greens",
#     legend=True
# )

us.plot(
    column="Electoral", ax=ax,
    cmap="Reds",
    legend=True
)
plt.title("Electoral Density", fontsize=20)

plt.show()