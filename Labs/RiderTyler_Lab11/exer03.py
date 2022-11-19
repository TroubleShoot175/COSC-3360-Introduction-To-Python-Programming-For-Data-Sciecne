# Lab 11 - Exercise 03

from matplotlib import pyplot as plt
from scipy import stats as s
import numpy as np

dataSet = [(-5, -10), (-1, -3), (3, 5), (7, 8), (5, 7), (9, 9)]
xValues = []
yValues = []

for i in range(len(dataSet)):
    xValues.append(dataSet[i][0])
    yValues.append(dataSet[i][1])

x = np.array(xValues)
y = np.array(yValues)
slope, yInt, r, p, std_err = s.linregress(x, y)
rL = (slope * x) + yInt

print(f'Slope: {slope}, y-intercept: {yInt}, Correlation (r): {r}, p-value: {p}, Standard Error: {std_err}')

plt.scatter(x, y)
plt.plot(x, rL)
plt.show()
