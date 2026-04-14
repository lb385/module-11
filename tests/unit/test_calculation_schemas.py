import pytest
from pydantic import ValidationError

from app.schemas.calculation import CalculationCreate, CalculationType


def test_calculation_create_accepts_valid_payload():
    calculation = CalculationCreate(a=10, b=5, type=CalculationType.ADD)

    assert calculation.a == 10
    assert calculation.b == 5
    assert calculation.type == CalculationType.ADD


def test_calculation_create_rejects_invalid_type():
    with pytest.raises(ValidationError):
        CalculationCreate(a=10, b=5, type="Unknown")


def test_calculation_create_rejects_divide_by_zero():
    with pytest.raises(ValidationError):
        CalculationCreate(a=10, b=0, type=CalculationType.DIVIDE)
