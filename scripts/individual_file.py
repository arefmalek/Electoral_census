import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import os

def p2f(s):
    try:
        return float(s)
    except ValueError:
        return 0

def alphabetize(dataframe):
    cols = dataframe.columns.tolist()
    cols = sorted(cols)
    cols.remove("Label")
    cols.insert(0, "Label")
    return dataframe[cols]

def processor(filename):
    data = pd.read_csv(filename)

    for column in data.columns:
        if column == "Label": continue
        if "Estimate" not in column:
            data = data.drop(column, axis=1)
    
    data = data.dropna()
    data.index = np.arange(len(data.index))

    # converting all strings to float (if they arent a number they become 0)
    for i in range(1, len(data.columns)):
        col = data.iloc[:, i].astype(str).str.replace('\D+', '').apply(p2f)
        data[data.columns[i]] = col

    # Renaming columns
    data.columns = (data.columns.str.replace("!!Estimate", ""))

    data = alphabetize(data)

    #removing as many 0 values as I can easily
    data = data[data["Alabama"] > 0]   

    #discarding PR for electoral vote file
    data = data.drop('Puerto Rico', axis = 1)
    #reindexing again to organize 
    data.index = np.arange(len(data.index))
    #copies comes in because now I can create the expected array rn
    copies = data.drop("Label", axis = 1)

    #expected array
    expected = copies.sum(axis=1) / copies.sum(axis = 1)[0] * 538

    #now splitting up data on a per-capita basis
    total_pop=data.iloc[0]

    for i in range(1, len(data.columns)):
        col = data.iloc[:, i] / total_pop[i]
        data[data.columns[i]] = col

    electorals = pd.read_csv("Data/state_data")
    diaspora = electorals["E.C. Votes"] 

    for i in range(1, len(data.columns)):
        col = data.iloc[:, i] * diaspora[i-1]
        data[data.columns[i]] = col

    #isolate the list of states to perform arithmetic on
    states = list(data)
    states.remove("Label")
    data[states]

    data["Expected"] = expected
    data["Actual"] = data[states].sum(axis=1)

    eva = pd.DataFrame({
    "Label": data.Label,
    "Delta": data.Actual - data.Expected
    })

    eva.index = data.Label.str.strip()

    #isolating data I want
    race = eva.loc["White alone":"Asian alone"].append(eva.loc["Hispanic or Latino (of any race)"])
    gender = eva.iloc[1:3]
    age = eva.loc["15 to 19 years": "75 to 84 years"]

    final  = race.append(age).append(gender)
    return final