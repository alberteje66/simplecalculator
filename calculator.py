#okay, going back to python for a bit

def add(x, y):
    print(x+y)
    pass

def subtract(x, y):
    print(x-y)
    pass

def multiply(x, y):
    print(x*y)

def divsion(x, y):
    try:
         print(x/y)
    except ZeroDivisionError:
        print("Can't divide by zero.\n")

def modulus(x, y):
    try:
        print(x%y)
    except ZeroDivisionError:
        print("Can't divide by zero.")

option = 1

print("1. Add \n 2. Subtract \n 3. Multiply \n 4. Divide and Modulus \n 0. Exit")
try:
    option = int(input("Choose an option: "))
except TypeError:
    print("Invalid selection.")
    pass

while option != 0:
    if option == 1:
        x = float(input("Enter two numbers: \n"))
        y= float(input())
        add(x, y)
    elif option == 2:
        x = float(input("Enter two numbers\n"))
        y= float(input())
        subtract(x, y)
    elif option == 3:
        x = float(input("Enter two numbers: \n"))
        y= float(input())
        multiply(x, y)
    elif option == 4:
        x = float(input("Enter two numbers \n"))
        y= float(input())
        divsion (x, y)
        modulus(x, y)
    elif option == 0:
        SystemExit("Good bye.")
    else: 
        print("Invalid option")
    break

    