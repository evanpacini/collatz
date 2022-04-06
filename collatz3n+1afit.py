import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from scipy.optimize import leastsq
import numpy as np
import csv
import os
import math
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


def err4pl(p, y, x):  # error
    err = y-l4p(x, *p)
    return err


def errlog(p, y, x):  # error
    err = y-logf(x, *p)
    return err


def l4p(x, A, B, C, D):  # 4-Paramter logistics
    return D + (A - D) / (1.0 + (x / C) ** B)


def logf(x, A, B, C):  # Log fit
    return A * np.log(x*C)/np.log(B)


p04pl = [0.0, 0.4, 1e-380, 33.3333333333]
c4pl, cov = leastsq(err4pl, p04pl, args=(y, x))
p0log = [1.0, 2.0, 1.0]
clog, cov = leastsq(errlog, p0log, args=(y, x))
print(*c4pl)
print(*clog)
ax = plt.figure("Collatz 3n+1 average percentage steps (" + N + ")").gca()
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
plt.plot(x, y, 'b-', label='Average % 3n+1 over seed', ms=1)
plt.hlines(y[n-2], 0, n, colors='g', linestyles='dashed',
           label='Average % 3n+1 (at max): '+str(y[n-2]))
plt.plot(x, l4p(x, *c4pl), 'k-', label='4PL fit')
plt.plot(x, logf(x, *clog), 'r-', label='Log fit')

plt.xlabel('Seed')
plt.ylabel('% 3n+1')
plt.title('Average percentage 3n+1 steps')
plt.legend()
plt.show()
