''' Lab 08 - Exercise 01 '''

import numpy as np
from matplotlib import pyplot as plt

x = np.arange(-1, 10, 0.1)
y = np.cos(x)

plt.plot(x, y, label="Cosine Wave", color="r")
plt.title("Consine Plot")
plt.legend(loc="lower left")
plt.show()
