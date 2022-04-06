# Collatz norm opt difference

import matplotlib.pyplot as plt
import numpy as np
import csv
import os
ynorm = []
yopt = []
N = input("N: ")
os.system("cpp\collatzsteps " + N)
os.system("cpp\collatz3n+1steps " + N)

with open('csv\collatzsteps.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        ynorm.append(int(row[1]))
with open('csv\collatz3n+1steps.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        yopt.append(int(row[1]))

y = np.array(ynorm)[1:] - np.array(yopt)[1:]
ylead = np.floor(y / 10 ** np.floor(np.log10(y)))

ax = plt.figure(
    "Collatz division 2 steps leading digit histogram (" + N + ")").gca()
plt.hist(ylead, bins=np.arange(11) - 0.5)
hist, binsize = np.histogram(ylead, bins=np.arange(11))
plt.plot(np.arange(10), hist, '-')
plt.xticks(range(1, 10))

plt.xlabel('Leading digit of steps')
plt.ylabel('Number of occurences')
plt.title('Number of occurences of leading digits of number of divisions by two')
plt.show()
