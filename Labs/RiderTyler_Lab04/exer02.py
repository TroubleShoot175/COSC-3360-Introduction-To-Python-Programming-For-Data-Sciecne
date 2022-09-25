''' Lab 04 - Exercise 02 '''
def is_vowel(letter):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for vowel in vowels:
        if letter == vowel:
            return True

userStr = input("Please enter a string: ")
print(list(filter(is_vowel, userStr)))
