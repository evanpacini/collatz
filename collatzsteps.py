import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np
import csv
import os
xarr = []
yarr = []
N = input("N: ")
os.system("cpp\collatzsteps " + N)

with open('csv\collatzsteps.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        xarr.append(int(row[0]))
        yarr.append(int(row[1]))

x = np.array(xarr)
y = np.array(yarr)
xlog = np.linspace(1, x.size, x.size)
ylog = np.log2(xlog)
mask1 = np.floor(np.log2(x)) == np.ceil(np.log2(x))

ax = plt.figure("Collatz steps normalised (" + N + ")").gca()
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.set_xscale('log', base=2)
plt.plot(xlog, ylog, '-', label='Log2', ms=3)
plt.plot(x, y, '.', label='Collatz', ms=1)
plt.plot(x[mask1], y[mask1], 'x', label='Powers of two')

plt.xlabel('Seed')
plt.ylabel('Steps')
plt.title('Seed VS Steps')
plt.legend()
plt.show()
