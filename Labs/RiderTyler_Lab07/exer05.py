''' Lab 07 - Exercise 04 '''

from cProfile import label
import matplotlib.pyplot as plt

COSC1310grades = {"HW1" : 35, "HW2" : 49, "HW3" : 74, "HW4" : 67, "HW5" : 75}
COSC3360grades = {"HW1" : 89, "HW2" : 93, "HW3" : 74, "HW4" : 82, "HW5" : 93}

fig, ax = plt.subplots(1, 2, figsize = (10, 5))

ax[0].plot(list(item for item in COSC1310grades), list(COSC1310grades.get(item) for item in COSC1310grades), color="b", label="1310 Grades", linewidth=5)
ax[0].legend(loc="upper left")
ax[0].set_title("Grades for COSC1310")
ax[0].set_xlabel("Homework Assignment")
ax[0].set_ylabel("Homework Grade")

ax[1].plot(list(item for item in COSC3360grades), list(COSC3360grades.get(item) for item in COSC3360grades), color="b", label="3360 Grades", linewidth=5)
ax[1].legend(loc="lower right")
ax[1].set_title("Grades for COSC3360")
ax[1].set_xlabel("Homework Assignment")
ax[1].set_ylabel("Homework Grade")

plt.ylim(0, 100)

plt.show()
