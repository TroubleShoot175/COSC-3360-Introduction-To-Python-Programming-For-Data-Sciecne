''' Lab 10 - Exercise 03 '''

from matplotlib import pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 2, 4, 4, 6])

m = ((np.mean(x*y)) - (np.mean(x) * np.mean(y))) / ((np.mean(x**2)) - (np.mean(x)**2))
b = np.mean(y) - (m * np.mean(x))
y1 = (b + (m * x))

plt.plot(x, y1, color='r')
plt.scatter(x, y)
plt.title("Least Squares Regression Line")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()

