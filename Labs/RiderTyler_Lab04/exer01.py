''' Lab 04 - Exercise 01 '''
def myFind(list, nFind):
    listIndex = []
    for num in range(0, len(list)):
        if list[num] == nFind:
            listIndex.append(num)
    return listIndex

numbers = [9, -3, 7, 2, 1, 2, 9, 9, 8, 2, 0, 0, 9, 2]
userNum = int(input("Please enter a number: "))
print(myFind(numbers, userNum))
