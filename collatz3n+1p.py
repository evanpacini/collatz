import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np
import csv
import os
xarr = []
yarr = []
N = input("N: ")
os.system("cpp\collatz3n+1p " + N)

with open('csv\collatz3n+1p.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        xarr.append(int(row[0]))
        yarr.append(float(row[1]))

x = np.array(xarr)
y = np.array(yarr)

ax = plt.figure("Collatz percentage 3n+1 steps normalised (" + N + ")").gca()
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.set_xscale('log', base=2)
plt.plot(x, y, '.', label='Collatz 3n+1 percentage', ms=1)

plt.xlabel('Seed')
plt.ylabel('% 3n+1')
plt.title('Percentage 3n+1 steps')
plt.legend()
plt.show()
