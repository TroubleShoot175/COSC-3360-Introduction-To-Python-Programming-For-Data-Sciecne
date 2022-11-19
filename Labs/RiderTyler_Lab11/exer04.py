# Lab 11 - Exercise 04

import numpy as np
from scipy import stats as s

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
sST = sum((y - np.mean(y)) ** 2)
sSR = sum((rL - np.mean(y)) ** 2)
sSE = sum((rL - y) ** 2)

print(f'SST: {sST}, SSR: {sSR}, SSE: {sSE}')
