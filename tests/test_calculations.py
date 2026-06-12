import pytest
from app.calculation import CalculationFactory
from app.calculator import CalculatorApp


@pytest.mark.parametrize(
    "operation,a,b,expected",
    [
        ("add", 2, 3, 5),
        ("+", 2, 3, 5),
        ("subtract", 5, 2, 3),
        ("-", 5, 2, 3),
        ("multiply", 4, 3, 12),
        ("*", 4, 3, 12),
        ("divide", 10, 2, 5),
        ("/", 10, 2, 5),
    ],
)
def test_calculation_factory(operation, a, b, expected):
    calculation = CalculationFactory.create(operation, a, b)
    assert calculation.result() == expected


def test_invalid_operation():
    with pytest.raises(ValueError):
        CalculationFactory.create("bad", 1, 2)


def test_calculation_string():
    calculation = CalculationFactory.create("add", 2, 3)
    assert str(calculation) == "2 + 3 = 5"


def test_calculator_parse_number():
    app = CalculatorApp()
    assert app.parse_number("5") == 5.0


def test_calculator_invalid_number():
    app = CalculatorApp()
    with pytest.raises(ValueError):
        app.parse_number("abc")


def test_calculator_calculate():
    app = CalculatorApp()
    assert app.calculate("add", "2", "3") == "Result: 5.0"
    assert len(app.history) == 1


def test_empty_history():
    app = CalculatorApp()
    assert app.show_history() == "No calculations yet."


def test_history():
    app = CalculatorApp()
    app.calculate("multiply", "2", "4")
    assert "2.0 * 4.0 = 8.0" in app.show_history()


def test_help():
    app = CalculatorApp()
    assert "Commands:" in app.show_help()