''' Lab 05 - Exercise 02 '''

li = [10, 'Hi', 20, 'Hello', 30, 'World', 40]

print(f"{list(map(lambda x : x * 2, filter(lambda i : True if type(i) != str else False, li)))}")
