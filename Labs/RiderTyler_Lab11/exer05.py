# Lab 11 - Exercise 05

from matplotlib import pyplot as plt
from scipy import stats as s
import numpy as np

hoursList = []
gradesList = []

with open('grades/grades.csv', mode='r') as gradesFile:
    for record in gradesFile:
        hoursStudied, grades = record.split(',')
        hoursList.append(float(hoursStudied))
        gradesList.append(float(grades))

x = np.array(hoursList)
y = np.array(gradesList)
slope, yInt, r, p, std_err = s.linregress(x, y)
rL = (slope * x) + yInt
pred = (slope * 10.5) + yInt

print(f'Slope: {slope}, y-intercept: {yInt}, Correlation (r): {r}, p-value: {p}, Standard Error: {std_err}, Prediction: {pred}')

plt.scatter(x, y)
plt.plot(x, rL)
plt.show()
