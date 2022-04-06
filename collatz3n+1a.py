import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np
import csv
import os
xarr = []
yarr = []
N = input("N: ")
n = int(N)
os.system("cpp\collatz3n+1a " + N)

with open('csv\collatz3n+1a.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        xarr.append(int(row[0]))
        yarr.append(float(row[1]))

x = np.array(xarr)
y = np.array(yarr)

ax = plt.figure("Collatz 3n+1 average percentage steps (" + N + ")").gca()
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
plt.plot(x, y, '-', label='Average % 3n+1 over seed', ms=1)
plt.hlines(y[n-2], 0, n, colors='g', linestyles='dashed',
           label='Average % 3n+1 (at max): '+str(y[n-2]))

plt.xlabel('Seed')
plt.ylabel('% 3n+1')
plt.title('Average percentage 3n+1 steps')
plt.legend()
plt.show()
