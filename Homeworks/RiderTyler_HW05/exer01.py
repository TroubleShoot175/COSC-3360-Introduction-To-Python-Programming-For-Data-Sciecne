''' Homework 05 - Exercise 01 '''
speed = int(input("Enter the speed of your vehicle in km/h: "))
distance = int(input("Enter the distance between your vehicle and the vehicle infront of you; in meters: "))

result = lambda speed, dist : (dist / (speed/3.6))

print(f'The time to collision is: {result(speed, distance)} seconds.')
