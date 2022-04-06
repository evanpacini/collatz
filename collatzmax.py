import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np
import csv
import os
xarr = []
yarr = []
N = input("N: ")
os.system("cpp\collatzmax " + N)

with open('csv\collatzmax.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        xarr.append(int(row[0]))
        yarr.append(int(row[1]))

x = np.array(xarr)
y = np.array(yarr)
mask1 = y < 5*int(N)

ax = plt.figure("Collatz peaks filtered (" + N + ")").gca()
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
plt.plot(x[mask1], y[mask1], '.', label='Collatz', ms=1)

plt.xlabel('Seed')
plt.ylabel('Peak value reached')
plt.title('Seed VS Max')
plt.legend()
plt.show()
