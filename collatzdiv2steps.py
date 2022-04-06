# Collatz norm opt difference

import matplotlib.pyplot as plt
import numpy as np
import csv
import os
ynorm = []
yopt = []
xarr = []
N = input("N: ")
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

y = np.array(ynorm) - np.array(yopt)
x = np.array(xarr)
xlog = np.linspace(1, x.size, x.size)
ylog = np.log2(xlog)
mask1 = np.floor(np.log2(x)) == np.ceil(np.log2(x))

ax = plt.figure("Collatz division 2 steps (" + N + ")").gca()
ax.set_xscale('log', base=2)
plt.plot(xlog, ylog, '-', label='Log2(x)', ms=3)
plt.plot(x, y, '.', label='Collatz divisions by two', ms=1)
plt.plot(x[mask1], y[mask1], 'x', label='Powers of two')

plt.legend()
plt.xlabel('Seed')
plt.ylabel('Δ Steps')
plt.title('Number of divisions by two')
plt.show()
