from datetime import datetime

from backend.core.base_response_schemas import ResponseBase


class QuadraticEquationResponse(ResponseBase):
    """Схема для отображения квадратного уравнения."""

    id: int
    value_a: int
    value_b: int
    value_c: int
    value_x1: float | None
    value_x2: float | None
    created_at: datetime
    updated_at: datetime
