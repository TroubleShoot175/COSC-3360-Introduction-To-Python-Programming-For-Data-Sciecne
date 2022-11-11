''' Lab 08 - Exercise 04 '''

import numpy as np
import pandas as pd

a = np.zeros((2, 4))

for x in range(0, 2):
    for y in range(0, 4):
        a[x][y] = int(input("Please enter an integer grade values: "))

a = a.flatten()

s = pd.Series(a)

print(s)
