def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):

    # prevent division by zero
    if b == 0:
        return "Cannot divide by zero"
    return a / b


def calculator():

    print("\nSimple Calculator")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")

    choice = input("Choose operation: ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        print("Result:", add(num1, num2))

    elif choice == "2":
        print("Result:", subtract(num1, num2))

    elif choice == "3":
        print("Result:", multiply(num1, num2))

    elif choice == "4":
        print("Result:", divide(num1, num2))

    else:
        print("Invalid choice")


# Run calculator
calculator()
