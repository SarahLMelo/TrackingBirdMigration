from matplotlib.ticker import Formatter
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np
from pandas._libs.tslibs import timestamps

birdData = pd.read_csv("bird_tracking.csv")
birdNames = pd.unique(birdData.bird_name)
stdColors = ["C0", "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9"]

#Pegando intervalo do tempo
timestamps = []
for i in range(len(birdData)):
    timestamps.append(datetime.datetime.strptime(birdData.date_time.iloc[i][:-3], "%Y-%m-%d %H:%M:%S"))

birdData["timestamps"] = pd.Series(timestamps, index = birdData.index)

plt.figure(figsize=(7, 7))

cnt = 1
for name in birdNames:
    times = birdData.timestamps[birdData.bird_name == name]
    firstTime = 0
    flag = 0
    elapsedTime = []
    plt.subplot(310+cnt)
    for time in times:
        if flag == 0:
            flag = 1
            firstTime = time
        elapsedTime.append(time-firstTime)

    plt.plot(np.array(elapsedTime)/datetime.timedelta(days=1), color = stdColors[cnt-1])
    plt.xlabel(" Observation ")
    plt.ylabel(" Elapsed time (days) ")
    plt.title(name)
    plt.tight_layout(pad = 3.0)
    cnt+=1

plt.show()