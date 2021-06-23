import pandas as pd
import dataframes as data
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import numpy as np
import os

def create_county(stat, county):
    df = data.create_countydf(stat, county)

    cols = list(df.columns)
    fig, ax = plt.subplots()

    the_file = os.path.dirname(os.path.abspath(__file__))
    tosavecounty = os.path.join(the_file, 'static/plots/')

    for i in range(0,len(cols)):
        plt.scatter(cols[i], df[cols[i]], c = 'black', s=5)

    xticks = ax.get_xticks()
    ax.set_xticks(xticks[::len(xticks) // 12])
    ax.margins(x=0)

    plt.xlabel('Date')
    plt.xticks(rotation=45)
    plt.ylabel(stat)
    if(stat == 'confirmed'):
        title = county + " County Covid Cases"
    elif(stat == 'deaths'):
        title = county + " County Covid Deaths"
    plt.title(title)

    title = county + "_" + stat + '.png'
    saveLocation = tosavecounty + title

    plt.savefig(saveLocation)
    return title


