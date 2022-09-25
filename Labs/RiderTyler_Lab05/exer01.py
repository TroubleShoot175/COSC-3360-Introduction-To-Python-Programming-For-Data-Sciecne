''' Lab 05 - Exercise 01 '''

tul1 = (1, 2, 3)
tul2 = (4, 5, 6)

print(tuple(map(lambda x : tul1[x]+tul2[x], range(0,len(tul1)))))
