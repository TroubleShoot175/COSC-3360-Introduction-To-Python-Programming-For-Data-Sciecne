''' Homework 04 - Exercise 03 '''

def isPrime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
            else:
                return True
    else:
        return False

numbers = [23, 2, 9, 7, 14, 18, 3, 24, 16, 5, 8, 97]
result = list(filter(isPrime, numbers))
print(result)
