''' Homework 05 - Exercise 03 '''
print("======= Convert =======")
print("1. Fahrenheit -> Celsius")
print("2. Celsius -> Fahrenheit")
print("=======================")

conSelect = int(input("Please select a converstion: "))
temp = float(input("Please enter a tempurature: "))

conver = lambda cS, temp : (temp - 32) * 5/9 if cS == 1 else (temp * 5/9) + 32
print(f'The converted tempurature is: {conver(conSelect, temp)}')
