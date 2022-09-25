''' Lab 05 - Exercise 06 '''

from functools import reduce

li = [10, 'Hi', 20, 'Hello', 30, 'World', 40]

print(f"{list(map(lambda x : x.upper(), filter(lambda i : True if type(i) == str else False, li)))}")
