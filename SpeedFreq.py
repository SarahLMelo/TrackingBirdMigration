import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

birdData = pd.read_csv("bird_tracking.csv")
birdNames = pd.unique(birdData.bird_name)
stdColors = ["C0", "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9"]

plt.figure(figsize=(9,9))
cnt = 1
for name in birdNames:
    i = birdData.bird_name == name
    speed = birdData.speed_2d[i]
    plt.subplot(310+cnt)
    plt.tight_layout(pad = 3.0)
    plt.title(name)
    plt.hist(speed, bins = np.linspace(0, 30, 20), density=True, color= stdColors[(cnt-1)%10])
    plt.xlabel(" 2D speed (m/s) ")
    plt.ylabel(" Frequency ")
    cnt+=1

plt.show()