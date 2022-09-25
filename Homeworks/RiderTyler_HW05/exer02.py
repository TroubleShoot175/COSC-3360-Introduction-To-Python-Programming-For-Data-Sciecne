''' Homework 05 - Exercise 02 '''
print("======= Convert =======")
print("1. Miles -> Kilometers")
print("2. Kilometers -> Miles")
print("=======================")

conSelect = int(input("Please select a converstion: "))
dist = float(input("Please enter a distance: "))

conver = lambda cS, dist : (dist * 1.609) if cS == 1 else (dist / 1.609)
print(f'The converted distance is: {conver(conSelect, dist)}')
