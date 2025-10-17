import art
import os

logo = art.logo

def add(n1, n2):
    return n1 + n2

def diff(n1, n2):
    return n1 - n2

def product(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operation = {
    "+" : add,
    "-" : diff,
    "*" : product,
    "/" : divide
}


def calculator():
    accumulate = True
    print(logo)
    n1 = float(input("Enter first number: "))

    while True:
        n2 = float(input("Enter second number: "))
        keys = list(operation.keys())
        print(keys)
        op = input("Choose an operation: ")
        answer = operation[op](n1, n2)
        print(f"{n1} {op} {n2} = {answer}")

        option = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if option == "y":
            n1 = answer
        else:
            accumulate = False
            os.system('clear')
            calculator()

calculator()