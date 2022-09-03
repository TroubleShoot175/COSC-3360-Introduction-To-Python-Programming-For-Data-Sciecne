''' Lab 02 - Exercise 03 '''

def myMinimum(num1=8, num2=2, num3=10):
    return min(num1, num2, num3)

print(f'Minimum with no parameters: {myMinimum()}')
print(f'Minimum with one parameter: {myMinimum(1)}')
print(f'Minimum with two parameters: {myMinimum(1, 2)}')
print(f'Minimum with three parameters: {myMinimum(1, 2, 3)}')
