# Lab 12 - Exercise 01

import numpy as np
import pandas as pd

# Read from CSV
df = pd.read_csv("auto-mpg.csv")

print(df.info())

df.mask(df == "?", other=np.nan, inplace=True)
df.dropna(axis=0, how='any', inplace=True)

print(df.info())
