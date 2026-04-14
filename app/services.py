from app.calculations.factory import CalculationFactory
from app.models.calculation import Calculation
from app.schemas.calculation import CalculationCreate


def build_calculation_record(payload: CalculationCreate) -> Calculation:
    result = CalculationFactory.calculate(payload.a, payload.b, payload.type)
    return Calculation(a=payload.a, b=payload.b, type=payload.type.value, result=result)
