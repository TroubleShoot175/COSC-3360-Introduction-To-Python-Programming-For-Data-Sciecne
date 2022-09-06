''' Homework 03 - Exercise 01 '''

x = int(input("Please enter a positive integer: "))

guess = x
nG = 1
eG = 0

while abs(nG - eG) > 0.00000001:
       eG = guess
       nG = (guess + (x / guess))/2
       guess = nG

print(f"The approximate square root of {x} is {guess}")