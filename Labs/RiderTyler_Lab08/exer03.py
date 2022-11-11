''' Lab 08 - Exercise 03 '''

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

a = np.zeros((2, 4))

for x in range(0, 2):
    for y in range(0, 4):
        a[x][y] = int(input("Please enter an integer grade values: "))

print(f'Updated Grade Array: \n{a}')

keyType = input("Please enter a semester to plot (Fall or Spring): ")
lineWidth = int(input("Please enter an integer for the line width: "))
uColor = input("Please enter a letter for color (r, b, g, y): ")

if keyType == "Fall":

    fallGrades = a[:1, :].reshape(4,)
    fallKeys = [0, 1, 2, 3]

    plt.plot(fallKeys, fallGrades, label="Grades", linewidth=lineWidth, color=uColor)
    plt.xlabel("Fall")
    plt.ylabel("Grades")
    plt.legend()
    

elif keyType == "Spring":
    
    springGrades = a[1:2, :].reshape(4,)
    springKeys = [0, 1, 2, 3]
    
    plt.plot(springKeys, springGrades, label="Grades", linewidth=lineWidth, color=uColor)
    plt.xlabel("Spring")
    plt.ylabel("Grades")
    plt.legend()

s = pd.Series(a.flatten())
print("Descriptive Statistics for Grades:\n", s.describe())

plt.title("Semester Grades")
plt.show()
