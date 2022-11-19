# Lab 11 - Exercise 02

from matplotlib import pyplot as plt
import numpy as np

dataSet = [(-5, -10), (-1, -3), (3, 5), (7, 8), (5, 7), (9, 9)]
xValues = []
yValues = []

for i in range(len(dataSet)):
    xValues.append(dataSet[i][0])
    yValues.append(dataSet[i][1])

x = np.array(xValues)
y = np.array(yValues)
w1 = ((np.mean(x*y)) - (np.mean(x) * np.mean(y))) / ((np.mean(x ** 2)) - (np.mean(x) ** 2))
w0 = np.mean(y) - (w1 * np.mean(x))
rL = w0 + (w1 * x)

plt.scatter(x, y)
plt.plot(x, rL)
plt.show()
