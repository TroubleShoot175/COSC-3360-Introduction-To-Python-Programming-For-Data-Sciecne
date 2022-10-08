''' Lab 06 - Exercise 01 '''

arr = [[77, 68, 86, 73], [96, 87, 89, 81], [70, 90, 86, 81]]

userThreshold = int(input("Please enter a threshold to filter integer array: "))

for list in range(0, len(arr)):
    for value in range(0, len(arr[list])):
        if arr[list][value] > userThreshold:
            arr[list][value] = 255
        else:
            arr[list][value] = 0

print("The new array is: ", arr)
