import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np
import csv
import os
xarr = []
yarr = []
N = input("N: ")
os.system("cpp\collatz3n+1steps " + N)

with open('csv\collatz3n+1steps.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        xarr.append(int(row[0]))
        yarr.append(int(row[1]))

x = np.array(xarr)
y = np.array(yarr)
mask1 = np.floor(np.log2(x)) == np.ceil(np.log2(x))

ax = plt.figure("Collatz 3n+1 steps (" + N + ")").gca()
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.set_xscale('log', base=2)
plt.plot(x, np.zeros(len(y)), '-', label='y = 0', ms=3)
plt.plot(x, y, '.', label='Collatz 3n+1', ms=1)
plt.plot(x[mask1], y[mask1], 'x', label='Powers of two')

plt.xlabel('Seed')
plt.ylabel('Steps')
plt.title('Number of 3n+1 steps')
plt.legend()
plt.show()
