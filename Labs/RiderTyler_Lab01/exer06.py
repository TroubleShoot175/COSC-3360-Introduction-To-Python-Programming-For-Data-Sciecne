''' Lab 01 - Exercise 06 '''

def mySquareRoot(num):
    if num < 0:
        num *= -1
    num = num ** 0.5
    print(num)

userNum = int(input("Please enter a integer: "))
mySquareRoot(userNum)
