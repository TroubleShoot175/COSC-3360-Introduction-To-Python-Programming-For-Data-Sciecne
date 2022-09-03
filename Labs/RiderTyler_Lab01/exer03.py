''' Lab 01 - Exercise 03 '''

userIn = 0
sum = 0

while userIn != -999:
    if userIn > 0:
        sum += userIn 
    userIn = float(input("Please enter a float number: "))

print(f"The sum of the numbers entered is: {sum}")
