''' Homework 05 - Exercise 05 '''

li = [9, "Robot", 3.14, 8, "Vision"]

print(f'{list(filter(lambda x : True if type(x) == str else False, li))}')
