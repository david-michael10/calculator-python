import art
logo = art.logo

def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide

}

should_continue = True
while should_continue:
    print(logo)

    number1 = float(input("What's the first number? "))
    print()
    print("+\n" "-\n" "*\n" "/\n")

    operation = input("Pick an operation: ")
    print()

    number2 = float(input("What's the next number? "))
    print()

    result = operations[operation] (number1,number2)
    print(f"{number1} {operation} {number2} = {result}")
    print()

    choice = input(f"Type 'y' to continue calculating with {result} or type 'n' to start a"
          f"new calculation: ").lower()

    while choice == "y":
        print()
        print("+\n" "-\n" "*\n" "/\n")

        operation = input("Pick an operation: ")
        print()

        number2 = float(input("What's the next number? "))
        print()

        previous_result = result
        result = operations[operation](result, number2)
        print(f"{previous_result} {operation} {number2} = {result}")
        print()

        choice = input(f"Type 'y' to continue calculating with {result} or type 'n' to start a"
                       f"new calculation: ").lower()
    print("\n" * 50)