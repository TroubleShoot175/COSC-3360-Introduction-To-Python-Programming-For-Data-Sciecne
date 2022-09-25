''' Lab 05 - Exercise 05 '''

from functools import reduce

li = [10, 'Hi', 20, 'Hello', 30, 'World', 40]

print(f"{reduce(lambda x, y : x if x < y else y, filter(lambda i : True if type(i) != str else False, li))}")
