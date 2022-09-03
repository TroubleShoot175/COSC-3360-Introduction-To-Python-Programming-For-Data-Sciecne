''' Lab 02 - Excercise 01 '''
import myFunctions as mF

userF1 = float(input("Please enter a float number: "))
userF2 = float(input("Please enter a second float number: "))

while True:
    oper = input("What operation would you like (+, -, *, /): ")
    if oper == "+":
        print(mF.addFun(userF1, userF2))
    elif oper == "-":
        print(mF.minusFun(userF1, userF2))
    elif oper == "*":
        print(mF.multiFun(userF1, userF2))
    elif oper == "/":
        print(mF.divideFun(userF1, userF2))
    else:
        print("Please enter an simple operation. (+, -, *, /)")
        