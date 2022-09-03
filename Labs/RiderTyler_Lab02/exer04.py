''' Lab 02 - Excercise 04 '''

def upperCaseCharacters(str):
    '''Prints letters that are capitalized and
        returns the total number of uppercase 
        characters in the given string.'''
    cnt = 0
    for letter in str:
        if 65 <= ord(letter) <= 90:
            print(letter)
            cnt += 1
    return cnt

myStr = input("Please enter a string: ")
print(f"The total number of upper case letters in your string is: {upperCaseCharacters(myStr)}")


