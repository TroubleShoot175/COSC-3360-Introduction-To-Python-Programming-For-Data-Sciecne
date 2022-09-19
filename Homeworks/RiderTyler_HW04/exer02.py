''' Homeowrk 04 - Exercise 02 '''

words = ['Anna', 'hELLo', 'rotor', 'wow', 'CS', 'kayAK', 'program-ming']

result = list(filter(lambda x: (x.upper() == ''.join(reversed(x.upper()))), words))

print(result)
