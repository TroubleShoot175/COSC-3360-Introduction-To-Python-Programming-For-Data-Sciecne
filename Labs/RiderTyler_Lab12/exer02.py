# Lab 12 -Exercise 02

import numpy as np
from statsmodels import api as sm
import pandas as pd
from matplotlib import pyplot as plt

# Read from CSV
df = pd.read_csv("auto-mpg.csv")

# Convert two columns 'weight' and 'mpg' to numpy arrays
x = (df[["weight"]].to_numpy()).flatten()
y = (df[["mpg"]].to_numpy()).flatten()

x = sm.add_constant(x)
model = sm.OLS(x, y).fit()
modPred = model.predict([range(1500, 5000, 500)])

plt.scatter(x, y)
plt.plot(x, np.array(model.fittedvalues))
plt.plot(x, np.array(modPred))
plt.show()
