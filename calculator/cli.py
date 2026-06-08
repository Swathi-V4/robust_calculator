from calculator.operations import Calculator


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_operation():
    valid_operations = ["add", "subtract", "multiply", "divide", "quit"]

    while True:
        operation = input(
            "Choose an operation (add, subtract, multiply, divide, quit): "
        ).lower()

        if operation in valid_operations:
            return operation

        print("Invalid operation.")


def run_calculator():
    calc = Calculator()

    print("Welcome to the Calculator!")

    while True:
        operation = get_operation()

        if operation == "quit":
            print("Goodbye!")
            break

        num1 = get_number("First number: ")
        num2 = get_number("Second number: ")

        try:
            if operation == "add":
                result = calc.add(num1, num2)
            elif operation == "subtract":
                result = calc.subtract(num1, num2)
            elif operation == "multiply":
                result = calc.multiply(num1, num2)
            else:
                result = calc.divide(num1, num2)

            print(f"Result: {result}")

        except ValueError as error:
            print(error)


if __name__ == "__main__":
    run_calculator()