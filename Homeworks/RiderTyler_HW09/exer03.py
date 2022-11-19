# Homework 09 - Exercise 03

# Libraries Imported
import numpy as np
from matplotlib import pyplot as plt


# Functions
def make_system_of(arr):
    length = len(arr)
    s = np.zeros((length, length))
    for r in range(length):
        for c in range(length):
            if c == 0:
                s[r, c] = 1
            else:
                s[r, c] = arr[r] ** c
    return s


# Convert Data set to two numpy arrays
dataSet = [(-2, 3), (-1, 5), (0, 1), (1, 4), (2, 10)]
xValues = []
yValues = []

for i in range(len(dataSet)):
    xValues.append(dataSet[i][0])
    yValues.append(dataSet[i][1])

x = np.array(xValues)
y = np.array(yValues)

# Make A Matrix
a = make_system_of(x)

# Print Coefficients
cArr = np.matmul(np.linalg.inv(a), y)
print(f'The polynomial coefficients are: {cArr}')

# Polynomial Solution
domain = np.linspace(np.min(x), np.max(x), len(x) * 10)
sol = 0

for i in range(len(cArr)):
    sol += cArr[i]*domain**i

# Plot the graph of the polynomial curve fit
plt.scatter(domain, sol, color="b", label='Points')
plt.plot(domain, sol, color='b', label='Curve Fit')

# Plot of the regular data set
plt.scatter(x, y, color="r", label='Points')
plt.plot(x, y, color='r', label='Plot')


# Show Plot
plt.title("Polynomial Curve Fitting")
plt.xlabel("X - Axis")
plt.xlabel("Y - Axis")
plt.legend()
plt.show()
