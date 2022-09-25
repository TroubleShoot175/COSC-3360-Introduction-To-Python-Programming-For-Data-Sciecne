''' Lab 04 - Exercise 04 '''
def greetingFunction(uName, greeting):
    print(greeting + " " + uName)

userName = input("Please enter your name: ")
userGreeting = input("Please enter a greeting: ")
greetingFunction(userName, userGreeting)

str = lambda uName, greeting : greeting + " " + uName
print(str(userName, userGreeting))
