''' Homework 01 - Exercise 02 '''

sum = 0
n = 0
while round(sum, 4) != 3.1415:
    sum += (-1)**n*(4/(2*n +1))
    n += 1
    print(f"Pi Approximated: {sum:.4f}, by term: {n}")
