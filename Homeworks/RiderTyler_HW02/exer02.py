''' Homework 02 - Exercise 02 '''

def myFind(word, charToFind):
    indexes = []
    occur = 0
    for letter in range(0, len(word)):
        if word[letter] == charToFind:
            indexes.append(letter)
    print(f"The indexes for the charater '{charToFind}' are {indexes}.")
    print(f"The number of times the letter '{charToFind}' appears in the string is {len(indexes)}.")

userStr = input("Please enter a string: ")
userChar = input("Please enter a character to find: ")
myFind(userStr, userChar)
