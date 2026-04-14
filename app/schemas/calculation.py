from enum import Enum

from pydantic import BaseModel, ConfigDict, Field, model_validator


class CalculationType(str, Enum):
    ADD = "Add"
    SUBTRACT = "Sub"
    MULTIPLY = "Multiply"
    DIVIDE = "Divide"


class CalculationBase(BaseModel):
    a: float = Field(..., description="Left operand")
    b: float = Field(..., description="Right operand")
    type: CalculationType = Field(..., description="Operation type")

    @model_validator(mode="after")
    def validate_division(self):
        if self.type == CalculationType.DIVIDE and self.b == 0:
            raise ValueError("b cannot be zero when type is Divide")
        return self


class CalculationCreate(CalculationBase):
    pass


class CalculationRead(CalculationBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    result: float
