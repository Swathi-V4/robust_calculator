import pytest
from unittest.mock import patch

from calculator.operations import Calculator
from calculator.cli import get_operation


@pytest.fixture
def calc():
    return Calculator()


def test_add(calc):
    assert calc.add(2, 3) == 5


def test_add_negative(calc):
    assert calc.add(-1, -1) == -2


def test_subtract(calc):
    assert calc.subtract(5, 3) == 2


def test_subtract_negative(calc):
    assert calc.subtract(-1, -1) == 0


def test_multiply(calc):
    assert calc.multiply(2, 3) == 6


def test_multiply_negative(calc):
    assert calc.multiply(-2, 3) == -6


def test_divide(calc):
    assert calc.divide(6, 2) == 3


def test_divide_float(calc):
    assert calc.divide(5, 2) == 2.5


def test_divide_by_zero(calc):
    with pytest.raises(ValueError):
        calc.divide(5, 0)


def test_get_operation_add():
    with patch("builtins.input", return_value="add"):
        assert get_operation() == "add"


def test_get_operation_subtract():
    with patch("builtins.input", return_value="subtract"):
        assert get_operation() == "subtract"


def test_get_operation_multiply():
    with patch("builtins.input", return_value="multiply"):
        assert get_operation() == "multiply"


def test_get_operation_quit():
    with patch("builtins.input", return_value="quit"):
        assert get_operation() == "quit"