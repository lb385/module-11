import pytest

from app.calculations.factory import CalculationFactory, AddOperation, DivideOperation, MultiplyOperation, SubtractOperation
from app.schemas.calculation import CalculationType


@pytest.mark.parametrize(
    ("calculation_type", "expected_class", "a", "b", "expected_result"),
    [
        (CalculationType.ADD, AddOperation, 2, 3, 5),
        (CalculationType.SUBTRACT, SubtractOperation, 8, 3, 5),
        (CalculationType.MULTIPLY, MultiplyOperation, 4, 5, 20),
        (CalculationType.DIVIDE, DivideOperation, 9, 3, 3),
    ],
)
def test_factory_returns_expected_operation_and_result(calculation_type, expected_class, a, b, expected_result):
    operation = CalculationFactory.get_operation(calculation_type)

    assert isinstance(operation, expected_class)
    assert CalculationFactory.calculate(a, b, calculation_type) == expected_result


def test_factory_rejects_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        CalculationFactory.calculate(5, 0, CalculationType.DIVIDE)
