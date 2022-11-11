''' Lab 10 - Exercise 01 '''

uStr = input("Please enter a string: ")

tokenStr = list(reversed(uStr.split(' ')))

reversedStr = str(' '.join(tokenStr))

print(f'Reversed Token: {reversedStr}')
