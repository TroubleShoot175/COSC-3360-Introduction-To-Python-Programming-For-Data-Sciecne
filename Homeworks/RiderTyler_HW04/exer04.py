''' Homework 04 - Exercise 04 '''

def str2Words(str):
    resultList = []
    list = []
    tempStr = ""
    list[:0] = str
    list[-1] = " "

    for letter in list:
        if letter != " " :
            tempStr = tempStr + letter
        else:
            resultList.append(tempStr)
            tempStr = ""
            
    return resultList

userStr = input("Please enter a sentence: ")
print(f"{str2Words(userStr)}")
