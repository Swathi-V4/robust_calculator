"""Arithmetic operation classes."""

class Operation:
    symbol = ""

    def execute(self, a: float, b: float) -> float:
        raise NotImplementedError


class Add(Operation):
    symbol = "+"

    def execute(self, a: float, b: float) -> float:
        return a + b


class Subtract(Operation):
    symbol = "-"

    def execute(self, a: float, b: float) -> float:
        return a - b


class Multiply(Operation):
    symbol = "*"

    def execute(self, a: float, b: float) -> float:
        return a * b


class Divide(Operation):
    symbol = "/"

    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b