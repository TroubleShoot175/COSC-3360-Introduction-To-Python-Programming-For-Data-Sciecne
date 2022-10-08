''' Lab 07 Exercise 03 '''

import matplotlib.pyplot as plt

uMin = int(input("Please enter a min number: "))
uMax = int(input("Please enter a max number: "))

x = list(range(uMin, uMax + 1))
y = list(abs(item) if item < 0 else item for item in x)

plt.plot(x, y)
plt.title("Plot For User Values")
plt.xlabel("User Entered Range")
plt.ylabel("Absoulte Value of User Entered Range")
plt.show()
