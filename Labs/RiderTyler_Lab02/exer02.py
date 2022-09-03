''' Lab 02 - Exercise 02 '''

def myFac(num):
    ''' Calculates and returns the 
    factorial of a given number.'''

    for x in range(num-1 , 0, -1):
        num *= x
    return num

e = 1

for x in range(1, 11):
    e += 1/myFac(x)

print(f'The number e is equal to: {e}')
