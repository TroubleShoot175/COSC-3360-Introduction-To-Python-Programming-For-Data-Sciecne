''' Lab 04 - Exercise 03 '''
def get_lower(letter):
    if  65 <= ord(letter) <= 90:
        return True

userStr = input("Please enter a string: ")
print(list(filter(get_lower, userStr))) 
