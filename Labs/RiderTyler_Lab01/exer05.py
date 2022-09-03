''' Lab 01 - Exercise 05 '''

def myPower(base, exponent):
    res = 1
    while exponent != 0:
        exponent -= 1
        res *= base
    print(res)

uBase = int(input("Please enter a base: "))
uExpo = int(input("Please enter a exponent: "))

myPower(uBase, uExpo)
