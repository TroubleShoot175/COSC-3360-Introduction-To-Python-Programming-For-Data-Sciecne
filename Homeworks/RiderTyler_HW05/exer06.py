''' Homework 05 - Exercise 06 '''

myLi = [3, 9.45, "Robotics", 8, 1]

print(f'{"".join(list(map(lambda letter : letter if 65 <= ord(letter) <= 90 else chr(ord(letter) - 32) , list(filter(lambda x : True if type(x) == str else False, myLi))[0])))}')
