''' Lab 04 - Exercise 01 '''
def get_vowels(letter):
    lTest = ord(letter)
    vowels = ["a", "e", "i", "o", "u"]
    for vowel in vowels:
        if lTest == vowel or lTest == ord(vowel) - 32:
            return letter

str = "Computer Science"

print(list(filter(get_vowels, list(str))))