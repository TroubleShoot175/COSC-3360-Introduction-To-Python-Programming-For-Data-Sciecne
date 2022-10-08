''' Lab 06 - Exercise 03 '''

def add_contact():
    global teleDic
    name = input("Please enter a name to add: ")
    number = input("Please enter a number to add: ")
    teleDic[name] = number

def remove_contact():
    global teleDic
    name = input("Please enter a name to remove: ")
    teleDic.pop(name)

def modify_contact():
    global teleDic
    name = input("Please enter a contact name to modify: ")
    nTemp = name
    nuTemp = teleDic[name]
    
    print("If for either item you wish not to change the item, enter a space.")
    name = input("Please enter the new contact name: ")
    number = input("Please enter the new number: ")

    if name == " " and number == " ":
        pass
    elif name != " " and number == " ":
        teleDic.pop(nTemp)
        teleDic[name] = nuTemp
    elif name == " " and number != " ":
        teleDic[nTemp] = number

def search_contacts():
    global teleDic
    name = input("Please enter a name to search: ")
    if name in teleDic:
        print('Found!')
        print(f'Name: {name}, Number: {teleDic[name]}')
    else:
        print("Not Found! :(")

def show_names():
    global teleDic
    names = teleDic.keys()
    for name in names:
        print(f'{name}', end=" ")
        print()


def show_numbers():
    global teleDic
    numbers = teleDic.values()
    for number in numbers:
        print(f'{number}', end=" ")
        print()

teleDic = {}

while True:
    # print("Telephone Dictionary: ", teleDic, end="\n")
    command = input("Please enter a command: ")
    if command == "add":
        add_contact()
    elif command == "remove":
        remove_contact()
    elif command == "modify":
        modify_contact()
    elif command == "search":
        search_contacts()
    elif command == "exit":
        break
    elif command == "show names":
        show_names()
    elif command == "show numbers":
        show_numbers()