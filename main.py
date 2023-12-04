import os
from art import logo


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def multi(a, b):
    return a * b


def div(a, b):
    return a / b


# storing all above function (add, sub,..) in operation as value
operation = {
    "+": add,
    "-": sub,
    "*": multi,
    "/": div
}


# Function does all the calculations
def Calculator():
    print(logo)
    print("Welcome to the Calculator!")

    n1 = float(input("What's the first number? \n"))
    n2 = float(input("What's the second number? \n"))
    print(" ")
    # iterating only key (+ - * /)
    for symbol in operation:
        print(symbol)

    operation_on = True

    # looping the program till user quits
    while operation_on:
        operation_symbol = input("What operation do you want to perform? \n")
        # 6 = {operation dictionary as *} [2, 3]
        result = operation[operation_symbol](n1, n2)

        print(f"{n1} {operation_symbol} {n2} = {result} \n\n")

        # taking the user input and checking their conditions
        user = input(
            f"Type 'y' to continue calculating with {result} or type 'n' to exit or type 'new' to start over again \n")
        if user == "y":
            n1 = result
            os.system('cls')
            n2 = float(input("What's the next number? \n"))
        elif user == "n":
            operation_on = False
        elif user == "new":
            os.system('cls')
            Calculator()


Calculator()