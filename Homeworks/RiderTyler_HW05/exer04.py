''' Homework 05 - Exercise 04 '''

def int_dataTypes(x):
    if type(x) == int:
        return True

li = [9, "Robot", 3.14, 8, "Vision"]

print(f'{list(filter(int_dataTypes, li))}')
