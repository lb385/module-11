from dataclasses import dataclass

from app.schemas.calculation import CalculationType


@dataclass(frozen=True)
class AddOperation:
    def calculate(self, a: float, b: float) -> float:
        return a + b


@dataclass(frozen=True)
class SubtractOperation:
    def calculate(self, a: float, b: float) -> float:
        return a - b


@dataclass(frozen=True)
class MultiplyOperation:
    def calculate(self, a: float, b: float) -> float:
        return a * b


@dataclass(frozen=True)
class DivideOperation:
    def calculate(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b


class CalculationFactory:
    _operations = {
        CalculationType.ADD: AddOperation(),
        CalculationType.SUBTRACT: SubtractOperation(),
        CalculationType.MULTIPLY: MultiplyOperation(),
        CalculationType.DIVIDE: DivideOperation(),
    }

    @classmethod
    def get_operation(cls, calculation_type: CalculationType):
        try:
            return cls._operations[calculation_type]
        except KeyError as exc:
            raise ValueError(f"Unsupported calculation type: {calculation_type}") from exc

    @classmethod
    def calculate(cls, a: float, b: float, calculation_type: CalculationType) -> float:
        operation = cls.get_operation(calculation_type)
        return operation.calculate(a, b)
