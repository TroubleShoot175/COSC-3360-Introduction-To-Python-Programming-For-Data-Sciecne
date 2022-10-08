''' Lab 07 - Exercise 04 '''

from cProfile import label
import matplotlib.pyplot as plt

COSC1310grades = {"HW1" : 35, "HW2" : 49, "HW3" : 74, "HW4" : 67, "HW5" : 75}
COSC3360grades = {"HW1" : 89, "HW2" : 93, "HW3" : 74, "HW4" : 82, "HW5" : 93}

plt.plot(list(item for item in COSC1310grades), list(COSC1310grades.get(item) for item in COSC1310grades), color="b", label="1310 Grades", linewidth=5)
plt.plot(list(item for item in COSC3360grades), list(COSC3360grades.get(item) for item in COSC3360grades), color="g", label="3360 Grades", linewidth=5)
plt.title("Grades for COSC1310 and COSC3360")
plt.xlabel("Homework Assignment")
plt.ylabel("Homework Grade")
plt.legend()

plt.ylim(0, 100)

plt.show()
