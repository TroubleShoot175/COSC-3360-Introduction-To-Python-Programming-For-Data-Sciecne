''' Homework 06 - Exercise 02 '''

import numpy as np
from matplotlib import pyplot as plt

uMin = int(input("Please enter a minimum number: "))
uMax = int(input("Please enter a maximum number: "))
uStep = int(input("Please enter a step number: "))

x = np.arange(uMin, uMax, uStep)

exp = input("Please enter an expression: ")

y = list(eval(exp) for x in x)

plt.plot(x, y, label="User Values", color="r")
plt.title("User Generated Plot")
plt.xlabel("User Entered Values")
plt.ylabel("Values After Evaluation")
plt.legend()
plt.show()
