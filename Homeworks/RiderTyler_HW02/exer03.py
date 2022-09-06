''' Homework 02 - Exercise 03 '''

def countWords(str):
    cnt = 0
    for char in str:
        if char == " ":
            cnt += 1
    return cnt + 1

userStr = input("Please enter a string: ")
print(f"The number of words in the string is: {countWords(userStr)}")
