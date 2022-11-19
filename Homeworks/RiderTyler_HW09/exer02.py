# Homework 09 - Exercise 02

# Libraries Imported
import numpy as np
from matplotlib import pyplot as plt

# Data for houses
houseSqFt = [250., 500, 1_000, 2_000, 3_000, 4_000]
housesPrices = [50_000., 100_000, 200_000, 400_000, 600_000, 800_000]

# Data For Houses to Numpy Array
xArr = np.array(houseSqFt)
x = np.array(list(zip(list(1 for i in range(len(houseSqFt))), houseSqFt)))
y = np.array(housesPrices)

# Create Noise derived from a standard normal (Gaussian) distribution
N = np.random.normal(0.0, 1.0, 6)

# Multiply the noise by 30,000 then add it to the dependent variable
rN = N * 30_000.

# Find the Least Squares Regression Line using Matrix Algebra
xT = x.T
xTXI = np.linalg.inv(np.matmul(xT, x))
xTY = np.matmul(xT, y)
a = np.matmul(xTXI, xTY)
rL = (a[1] * xArr) + a[0]

# Adding Noise to dependent variable
rLWN = (a[0] + (a[1] * xArr)) + rN

# Verify the line is the same as the regression line that is gotten in the first example
w1 = ((np.mean(xArr * y)) - (np.mean(xArr) * np.mean(y))) / ((np.mean(xArr ** 2)) - (np.mean(xArr) ** 2))
w0 = np.mean(y) - (w1 * np.mean(xArr))
rLV = (w1 * xArr) + w0

result = np.array_equal(rL, rLV)
print(f'Does this regression lines match Exercise 1 regression line: {"Yes" if result else "No"}')

# Plot the Noise Addition
plt.plot(xArr, rLWN, color='r')

# Plot the regression line
plt.plot(xArr, rL, color='b')

# Show Plot
plt.show()

# Print Results
print("Standard Value Results:")
for i in range(len(xArr)):
    print(f'Standard X:{xArr[i]} | Standard Y: {y[i]}')

print()

print("Standard Value With Regression Line:")
for i in range(len(xArr)):
    print(f'Standard X:{xArr[i]} | Regression Y: {rL[i]}')

print()

print("Standard Value With Noise Results:")
for i in range(len(xArr)):
    print(f'Standard X:{xArr[i]} | Noise Added Y: {rLWN[i]}')

print()

print("Regression Lines (Because they did not match): ")
print(f'Regression Line Exercise One: {rLV} | Regression Line Exercise Two: {rL}')
