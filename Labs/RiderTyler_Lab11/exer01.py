# Lab 11 - Exercise 1

from matplotlib import pyplot as plt
import numpy as np

dataSet = [(-5, -10), (-1, -3), (3, 5), (7, 8), (5, 7), (9, 9)]
xValues = []
yValues = []

for i in range(len(dataSet)):
    xValues.append(dataSet[i][0])
    yValues.append(dataSet[i][1])

xArr = np.array(xValues)
x = np.array(list(zip(list(1 for i in range(len(xValues))), xValues)))
y = np.array(yValues)
xT = x.T
xTXI = np.linalg.inv(np.matmul(xT, x))
xTY = np.matmul(xT, y)
a = np.matmul(xTXI, xTY)
rL = a[0] + (a[1] * xArr)

plt.scatter(xValues, yValues)
plt.plot(xValues, rL)
plt.show()
