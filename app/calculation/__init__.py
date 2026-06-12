"""Calculation models and factory."""

from app.operation import Add, Subtract, Multiply, Divide


class Calculation:
    """Represents one calculation."""

    def __init__(self, operation, a: float, b: float):
        self.operation = operation
        self.a = a
        self.b = b

    def result(self) -> float:
        return self.operation.execute(self.a, self.b)

    def __str__(self) -> str:
        return f"{self.a} {self.operation.symbol} {self.b} = {self.result()}"


class CalculationFactory:
    """Creates calculations based on user input."""

    operations = {
        "add": Add,
        "+": Add,
        "subtract": Subtract,
        "-": Subtract,
        "multiply": Multiply,
        "*": Multiply,
        "divide": Divide,
        "/": Divide,
    }

    @classmethod
    def create(cls, operation_name: str, a: float, b: float) -> Calculation:
        key = operation_name.lower()

        if key not in cls.operations:
            raise ValueError("Invalid operation.")

        operation = cls.operations[key]()
        return Calculation(operation, a, b)