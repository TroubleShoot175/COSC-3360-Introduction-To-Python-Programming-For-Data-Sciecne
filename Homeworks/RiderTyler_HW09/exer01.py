# Homework 09 - Exercise 01

# Libraries imported
import numpy as np
from matplotlib import pyplot as plt

# Data for houses
houseSqFt = [250., 500, 1_000, 2_000, 3_000, 4_000]
housesPrices = [50_000, 100_000, 200_000, 400_000, 600_000, 800_000]
houseSqFtToPredict = [200., 1_250, 2_710, 5_100]
x = np.array(houseSqFt)
y = np.array(housesPrices)
predX = np.array(houseSqFtToPredict)

# Create Noise derived from a standard normal (Gaussian) distribution
N = np.random.normal(0.0, 1.0, 6)

# Multiply the noise by 30,000 then add it to the dependent variable
rN = N * 30_000

# Use Ordinary Least Squares to find the regression line parameters
w1 = ((np.mean(x*y)) - (np.mean(x) * np.mean(y))) / ((np.mean(x ** 2)) - (np.mean(x) ** 2))
w0 = np.mean(y) - (w1 * np.mean(x))
rL = (w1 * x) + w0
rLWN = ((w1 * x) + w0) + rN

# Estimate the Sum of Squared Error (SSE) and Find the Correlation Coefficient
sSE = sum((rL - y) ** 2)

# Calculate the predicted values based on the House square footage
predY = []

for price in houseSqFtToPredict:
    predY.append((w1 * price) + w0)

# Plot the data points
plt.scatter(x, y)

# Plot the Noise Addition
plt.plot(x, rLWN, color='r')

# Plot the regression line
plt.plot(x, rL, color='b')

# Plot the predicted house prices
plt.plot(predX, np.array(predY), color='g')

# Show Plot
plt.show()

# Print Results
print("Standard Value Results:")
for i in range(len(x)):
    print(f'Standard X:{x[i]} | Standard Y: {y[i]}')

print()

print("Standard Value With Regression Line:")
for i in range(len(x)):
    print(f'Standard X:{x[i]} | Regression Y: {rL[i]}')

print()

print("Standard Value With Noise Results:")
for i in range(len(x)):
    print(f'Standard X:{x[i]} | Noise Added Y: {rLWN[i]}')

print()

print("Prediction Results:")
for i in range(len(predX)):
    print(f'Prediction X:{predX[i]} | Prediction Y: {predY[i]}')
