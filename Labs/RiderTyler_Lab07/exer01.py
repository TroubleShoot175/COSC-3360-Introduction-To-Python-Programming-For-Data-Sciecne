''' Lab 07 - Exercise 02'''

def set_add():
    global setA, setB
    setSel = input("Please select a set (A or B): ")
    elem = int(input("Please enter a element to add: "))
    
    if setSel == "A":
        setA.add(elem)
    else:
        setB.add(elem)

def set_remove():
    global setA, setB
    setSel = input("Please select a set: ")
    elem = int(input("Please enter a element to add: "))

    if setSel == "A":
        setA.remove(elem)
    else:
        setB.remove(elem)

def set_union():
    global setA, setB
    print("Union: ", setA.union(setB))
    pass

def set_intersection():
    global setA, setB
    print("Intersection: ", setA.intersection(setB))

def set_difference():
    global setA, setB
    print("Difference: ", setA.difference(setB))

def set_symdiff():
    global setA, setB
    print("Symmetric Difference: ", setA.symmetric_difference(setB))

def set_disjoint():
    global setA, setB
    print("Disjoint: ", setA.isdisjoint(setB))
    pass

li = list(range(10, 21))

setA = set(li)
setB = set(item for item in li if item % 2)

while True:
    print(setA)
    print(setB)
    print()
    userOp = input("Please enter a command: ")
    if userOp == "add":
        set_add()
    elif userOp == "remove":
        set_remove()
    elif userOp == "union":
        set_union()
    elif userOp == "intersection":
        set_intersection()
    elif userOp == "difference":
        set_difference()
    elif userOp == "symmetric difference":
        set_symdiff()
    elif userOp == "disjoint":
        set_disjoint()
    else:
        print("Please enter a command.")
