''' Lab 10 - Exercise 02 '''

uStr = input("Please enter a string: ")

tokenizedStr = uStr.split(" ")

for string in tokenizedStr:
    if string[-2] + string[-1] == 'ed':
        print(string)

