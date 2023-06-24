from pydantic import validator

from backend.core.base_request_schemas import RequestBase


class QuadraticEquationRequest(RequestBase):
    """Схема для квадратного уравнения."""

    value_a: int
    value_b: int
    value_c: int

    @validator('value_a')
    def validate_value_a(cls, value: int) -> int:
        if value == 0:
            raise ValueError("Значение A должно быть отлично от нуля.")
        return value


class QuadraticEquationCreateRequest(QuadraticEquationRequest):
    """Схема для создания квадратного уравнения."""

    pass
