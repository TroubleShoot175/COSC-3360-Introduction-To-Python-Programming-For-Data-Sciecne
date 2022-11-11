''' Homework 08 - Exercise 03 '''

from operator import index
from matplotlib import pyplot as plt
import pandas as pd

grades_dict = {'Wally' : [87, 96, 70], 'Eva' : [100, 87, 90], 
              'Sam' : [94, 77, 90], 'Katie' : [100, 81, 82], 
              'Bob' : [83, 65, 85]}

grades = pd.DataFrame(grades_dict)
studList = []

for s in grades:
    li = grades.T.loc[s]
    studList.append(li)

plt.plot(studList, label=["Test One", "Test Two", "Test Three"])
plt.xticks(list(i for i in range(len(grades.T.index))), list(name for name in grades))
plt.title("Student Grades")
plt.xlabel("Student")
plt.ylabel("Grades")
plt.legend(loc="lower left")
plt.ylim(0, 100)
plt.show()

