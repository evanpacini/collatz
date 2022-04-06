import matplotlib.pyplot as plt
import numpy as np
import csv
import os
yarr = []
N = input("N: ")
os.system("cpp\collatzsteps " + N)

with open('csv\collatzsteps.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        yarr.append(int(row[1]))

y = np.array(yarr)
ylead = np.floor(y / 10 ** np.floor(np.log10(y)))

plt.figure("Collatz steps leading digit histogram (" + N + ")")
plt.hist(ylead, bins=np.arange(11) - 0.5)
hist, binsize = np.histogram(ylead, bins=np.arange(11))
plt.plot(np.arange(10), hist, '-')
plt.xticks(range(1, 10))

plt.xlabel('Leading digit of steps')
plt.ylabel('Number of occurences')
plt.title('Number of occurences of leading digits of number of steps')
plt.show()
