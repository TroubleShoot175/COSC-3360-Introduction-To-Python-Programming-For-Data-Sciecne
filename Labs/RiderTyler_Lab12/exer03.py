# Lab 12 - Exercise 03

from matplotlib import pyplot as plt
import pandas as pd

# Read from CSV
df = pd.read_csv("housing.csv")

# df columns to numpy array
x = df[["Longitude"]].to_numpy()
y = df[["Latitude"]].to_numpy()

# K-Means Clustering
k = 6

# Plot
plt.scatter(x, y)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()

