''' Lab 07 Exercise 02 '''

def print_2DList():
    global li
    for index in range(0, len(li)):
        print(li[index])

li = [[1, 5], 
      [4, 10], 
      [9, 6]]

print_2DList()

uRow = int(input("Which row would you like to edit: "))
uCol = int(input("Which coloumn would you like to edit: "))
uElem = int(input("Please enter a new element to add to the array: "))

li[uRow - 1][uCol - 1] = uElem

print_2DList()
