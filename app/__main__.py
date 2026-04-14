from app.schemas.calculation import CalculationCreate, CalculationType
from app.services import build_calculation_record


def main() -> None:
    payload = CalculationCreate(a=8, b=2, type=CalculationType.DIVIDE)
    calculation = build_calculation_record(payload)
    print(
        "Module 11 calculation service ready: "
        f"{calculation.a} {calculation.type} {calculation.b} = {calculation.result}"
    )


if __name__ == "__main__":
    main()
