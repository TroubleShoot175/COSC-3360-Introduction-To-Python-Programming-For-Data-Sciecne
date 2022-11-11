''' Lab 08 - Exercise 02 '''

import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(-1, 10, num=120)
y = np.tan(x)

plt.plot(x, y, label="Tangent Wave", color="r")
plt.title("Tangent Plot")
plt.legend(loc="lower left")
plt.show()
