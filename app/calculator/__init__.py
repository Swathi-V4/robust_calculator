"""Calculator REPL application."""

from app.calculation import CalculationFactory


class CalculatorApp:
    """Command-line calculator with history and commands."""

    def __init__(self):
        self.history = []

    def show_help(self) -> str:
        return (
            "Commands:\n"
            "add, subtract, multiply, divide\n"
            "+, -, *, /\n"
            "history - show past calculations\n"
            "help - show instructions\n"
            "exit - quit"
        )

    def show_history(self) -> str:
        if not self.history:
            return "No calculations yet."
        return "\n".join(str(item) for item in self.history)

    def parse_number(self, value: str) -> float:
        try:  # EAFP
            return float(value)
        except ValueError as exc:
            raise ValueError("Please enter a valid number.") from exc

    def calculate(self, operation: str, first: str, second: str) -> str:
        a = self.parse_number(first)
        b = self.parse_number(second)

        calculation = CalculationFactory.create(operation, a, b)
        result = calculation.result()

        self.history.append(calculation)
        return f"Result: {result}"

    def run(self):  # pragma: no cover
        print("Professional Calculator")
        print("Type help for commands.")

        while True:
            operation = input("\nEnter operation: ").strip()

            if operation.lower() == "exit":
                print("Goodbye!")
                break

            if operation.lower() == "help":
                print(self.show_help())
                continue

            if operation.lower() == "history":
                print(self.show_history())
                continue

            first = input("Enter first number: ")
            second = input("Enter second number: ")

            try:
                print(self.calculate(operation, first, second))
            except Exception as error:
                print(f"Error: {error}")