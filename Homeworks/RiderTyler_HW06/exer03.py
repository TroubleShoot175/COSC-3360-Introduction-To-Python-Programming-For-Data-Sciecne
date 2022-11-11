''' Homework 06 - Exercise 03 '''

import statistics as s
import numpy as np

a = np.zeros([2, 4])

for x in range(0, 2):
    for y in range(0, 4):
        if x == 0:
            userIn = int(input("Please enter a fall semester grade: "))
            a[x][y] = userIn
        elif x == 1:
            userIn = int(input("Please enter a spring semester grade: "))
            a[x][y] = userIn
        
aTop = a[:1, :]
aBottom = a[1:2, :]

b = a.reshape(4, 2)

rA = b[:, 1:]
lA = b[:, :1]

print(f'Fall Semester Grade Info: Minimum: {min(aTop)}, Maximum: {max(aTop)}, Mean: {s.mean(list(aTop))}, Standard Deviation:{s.stdev(aTop)}')
print(f'Spring Semester Grade Info: Minimum: {min(aBottom)}, Maximum: {max(aBottom)}, Mean: {s.mean(list(aBottom))}, Standard Deviation:{s.stdev(aBottom)}')
