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
        if "!!Total!!Estimate" not in column:
            data = data.drop(column, axis=1)
    
    data = data.dropna()
    data.index = np.arange(len(data.index))

    # converting all strings to float (if they arent a number they become 0)
    for i in range(1, len(data.columns)):
        col = data.iloc[:, i].astype(str).str.replace('\D+', '').apply(p2f)
        data[data.columns[i]] = col

    # Renaming columns
    data.columns = (data.columns.str.replace("!!Total!!Estimate", ""))

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

    electorals = pd.read_csv("Data\state_data")
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
    return eva

def comparison(start, end, data, title):
    ax = sns.barplot(x=data.Label[start:end], y=data.Delta[start:end])
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
    ax.set_xlabel(title)
    return ax

def race(data):
    return comparison(7, 13, data, "Race")

def gender(data):
    return comparison(5,7,data, "Sex")

def poverty(data):
    return comparison(24,26,data,"Poverty Line")

def education(data):
    return comparison(14,23,data,"Education Level")