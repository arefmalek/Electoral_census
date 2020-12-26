import pandas as pd
import seaborn as sns

def df_creator(start, end):
    comp = pd.DataFrame()
    for number in range(start, end):
        comp[str(number)] = processor("Data\\{}_full.csv".format(number)).Delta
    comp.insert(0, "Label", processor("Data/2017_full.csv").Label)
    return comp

def plotter(data, start, end, plot_topic):
    temp = data[start:end]
    temp = temp.set_index("Label")
    temp = temp.transpose()

    sns.set(rc={'figure.figsize':(12,8)})

    # sns.set(style="whitegrid") #White background 
    sns.set_style("darkgrid", {"axes.facecolor": ".9"}) #grey background

    g = sns.lineplot(data = temp,linestyle = '-', linewidth = 3)
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

    #axis line at y=0
    g.axhline(0, color = 'black', linewidth = 3)

    #labels + title
    g.set_title("Electoral College Votes Disparity by " + plot_topic, size=24)
    g.set(xlabel='Year', ylabel= "Electoral Votes Difference")
    return g

def race(data):
    return plotter(data, 8, 14, "Race")

def gender(data):
    return plotter(data,5,7, "Sex")

def poverty(data):
    return plotter(data,24,26,"Poverty Line")

def education(data):
    return plotter(data,14,21,"Education Level")