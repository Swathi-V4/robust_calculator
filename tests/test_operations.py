import pytest
from app.operation import Operation, Add, Subtract, Multiply, Divide


def test_base_operation():
    operation = Operation()

    with pytest.raises(NotImplementedError):
        operation.execute(1, 2)


@pytest.mark.parametrize(
    "operation,a,b,expected",
    [
        (Add(), 2, 3, 5),
        (Subtract(), 5, 2, 3),
        (Multiply(), 4, 3, 12),
        (Divide(), 10, 2, 5),
    ],
)
def test_operations(operation, a, b, expected):
    assert operation.execute(a, b) == expected


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Divide().execute(10, 0)