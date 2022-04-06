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

y = np.array(ynorm) - np.array(yopt)

ax = plt.figure("Collatz division 2 step histogram (" + N + ")").gca()
plt.hist(y, bins=np.arange(y.min(), y.max()+1)-0.5)

plt.xlabel('Number of steps')
plt.ylabel('Number of occurences')
plt.title('Occurences of number of divisions by two')
plt.show()
