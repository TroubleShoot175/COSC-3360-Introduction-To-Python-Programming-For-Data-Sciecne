''' Lab 03 - Excercise 02 '''

li = [9, 3, 0, -4, 8, 7, 10, -1, 5]
list = []

useStrt = (int(input("Please enter a starting index on the list: ")) - 1)
useStop = (int(input("Please enter a finishing index for the list: ")) - 1)
useStep = int(input("Please enter the step between numbers in the list: "))

li = li[useStrt:useStop]

cnt = 0
for x in range(0, len(li)):
    cnt += 1
    if cnt == useStep:
        cnt = 0
        list.append(li[x])

print(list)
