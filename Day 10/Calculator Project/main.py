# Calculator

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calculation = {"+": add,
               "-": subtract,
               "*": multiply,
               "/": divide,
}
from art import logo


def calculator():
    print(logo)
    calculating = True
    n1 =  float(input("What's the first number?: "))

    while calculating:
        for symbol in calculation:
            print(symbol)
        operator = input('What\'s the operator?: "+" "-" "*" "/"? ')
        n2 = float(input("What's the second number?: "))
        answer = calculation[operator](n1, n2)

        print(f"{n1} {operator} {n2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or Type 'n' to start a new calculation: ").lower()
        if choice == "y":
            n1 = answer
        elif choice == "n":
            calculating = False
            print("\n" * 250)
            calculator()

calculator()