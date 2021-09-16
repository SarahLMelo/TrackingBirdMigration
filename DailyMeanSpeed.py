import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np

birdData = pd.read_csv("bird_tracking.csv")
birdNames = pd.unique(birdData.bird_name)
stdColors = ["C0", "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9"]

timestamps = []
for i in range(len(birdData)):
    timestamps.append(datetime.datetime.strptime(birdData.date_time.iloc[i][:-3], "%Y-%m-%d %H:%M:%S"))

birdData["timestamps"] = pd.Series(timestamps, index = birdData.index)

plt.figure(figsize=(10,10))

cnt = 1
lastIndex = 0
possibleLastIndex = 0
for name in birdNames:
    plt.subplot(310+cnt)

    data =  birdData[birdData.bird_name == name]
    times = data.timestamps
    flag = 0
    firstDay = 0
    elapsedTime = []
    for time in times:
        if flag == 0:
            flag = 1
            firstDay = time

        elapsedTime.append(time-firstDay)
    elapsedDays = np.array(elapsedTime)/datetime.timedelta(days=1)

    nextDay = 1
    inds = []
    dailyMeanSpeed = []
    for (i,t) in enumerate(elapsedDays):
        possibleLastIndex = i+lastIndex
        if t<nextDay:
            inds.append(i+lastIndex)
        else:
            dailyMeanSpeed.append(np.mean(data.speed_2d[inds]))
            nextDay+=1
            inds = []
    lastIndex = possibleLastIndex+1

    plt.plot(dailyMeanSpeed, "s-", color = stdColors[(cnt-1)%10])
    plt.title(name)
    plt.xlabel(" Day ")
    plt.ylabel(" Mean Speed (m/s) ")
    plt.tight_layout(pad = 3.0)

    cnt+=1

plt.show()