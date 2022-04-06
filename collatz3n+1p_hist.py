# Collatz 3n+1 percentage

import matplotlib.pyplot as plt
import numpy as np
import csv
import os
ynorm = []
yopt = []
xarr = []
N = input("N: ")
n = int(N)
os.system("cpp\collatzsteps " + N)
os.system("cpp\collatz3n+1steps " + N)

with open('csv\collatzsteps.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        ynorm.append(int(row[1]))
        xarr.append(int(row[0]))
with open('csv\collatz3n+1steps.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        yopt.append(int(row[1]))

y = np.array(yopt)[1:] / np.array(ynorm)[1:] * 100
x = np.array(xarr)[1:]
ystd = np.std(y)
ymean = np.mean(y)
ymed = np.median(y)

ax = plt.figure("Collatz 3n+1 percentage (" + N + ")").gca()
plt.hlines(ymean, 0, n, colors='g',
           label='Mean: ' + str(ymean))
plt.fill_between(x, ymean - ystd, ymean + ystd, alpha=0.5,
                 label='Standard deviation: '+str(ystd), zorder=5)
plt.hlines(ymed, 0, n, colors='r',
           label='Median: ' + str(ymed))
if n <= 1000:
    plt.bar(x, y, align='center', width=1)
else:
    idx = np.round(np.linspace(0, len(y) - 1, 1000)).astype(int)
    plt.bar(x[idx], y[idx], align='center', width=n/1000)
plt.legend()
plt.xlabel('Seed')
plt.ylabel('% Steps')
plt.title('Percentage of 3n+1 steps for each seed')
plt.show()
