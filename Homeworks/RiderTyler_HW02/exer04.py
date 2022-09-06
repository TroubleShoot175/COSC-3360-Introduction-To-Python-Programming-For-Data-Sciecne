''' Homework 02 - Exercise 04 '''

def myToUpper(str):
    for letter in range(0, len(str)):
        if 97 <= ord(str[letter]) <= 122:
            str[letter] = chr(ord(str[letter]) - 32)
    return str
    
userStr = list(input("Please enter a string: "))
print(myToUpper(userStr))
