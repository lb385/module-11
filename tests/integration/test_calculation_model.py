import pytest
from sqlalchemy import select
from pydantic import ValidationError

from app.calculations.factory import CalculationFactory
from app.models.calculation import Calculation
from app.schemas.calculation import CalculationCreate, CalculationType
from app.services import build_calculation_record


def test_can_insert_and_read_calculation(session):
    payload = CalculationCreate(a=12, b=4, type=CalculationType.DIVIDE)
    calculation = build_calculation_record(payload)

    session.add(calculation)
    session.commit()
    session.refresh(calculation)

    stored = session.scalar(select(Calculation).where(Calculation.id == calculation.id))

    assert stored is not None
    assert stored.a == 12
    assert stored.b == 4
    assert stored.type == "Divide"
    assert stored.result == 3


def test_invalid_division_is_rejected_before_insert():
    with pytest.raises(ValidationError):
        CalculationCreate(a=12, b=0, type=CalculationType.DIVIDE)


def test_service_builds_matching_result():
    payload = CalculationCreate(a=9, b=3, type=CalculationType.ADD)
    calculation = build_calculation_record(payload)

    assert calculation.result == CalculationFactory.calculate(9, 3, CalculationType.ADD)
