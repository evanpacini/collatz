import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np
import csv
import os
yarr = []
N = input("N: ")
os.system("cpp\collatzsteps " + N)

with open('csv\collatzsteps.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        yarr.append(int(row[1]))

y = np.array(yarr)

ax = plt.figure("Collatz step histogram (" + N + ")").gca()
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
plt.hist(y, bins=np.arange(y.min(), y.max()+1)-0.5)

plt.xlabel('Number of steps')
plt.ylabel('Number of occurences')
plt.title('Number of occurences of specific number of steps')
plt.show()
