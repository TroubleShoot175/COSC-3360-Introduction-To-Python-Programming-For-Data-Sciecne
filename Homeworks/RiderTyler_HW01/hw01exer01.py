''' Homework 01 - Excercise 01 '''

def myFactorialWithForLoop(x):
    for num in range(x-1, 0, -1):
        x *=num
    print(f"Factorial with For Loop: {x}")

def myFactorialWithWhileLoop(x):
    c = x - 1
    while c != 1:
        x *= c
        c-=1
    print(f"Factorial with While Loop: {x}")


userInt = int(input("Please enter a integer: "))
myFactorialWithForLoop(userInt)
myFactorialWithWhileLoop(userInt)
