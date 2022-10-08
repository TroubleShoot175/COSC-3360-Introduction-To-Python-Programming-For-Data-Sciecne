'''  Lab 06 - Exercise 02 '''
names = []
heights = []
weights = []

while len(weights) != 3:
    uName = input("Please enter a name: ")
    names.append(uName)
    uHeight = input("Please enter a height: ")
    heights.append(uHeight)
    uWeight = input("Please enter a weight: ")
    weights.append(uWeight)


peopleInfo = list(zip(names, heights, weights))

print(f'{peopleInfo}')
