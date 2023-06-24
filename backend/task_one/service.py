import math
from typing import Optional

from fastapi import Depends
from backend.task_one.models import QuadraticEquation

from backend.task_one.repository import QuadraticEquationRepository
from backend.task_one.request_schemas import QuadraticEquationCreateRequest


class QuadraticEquationService:
    """Сервис для работы с квадртаными выражениями."""

    def __init__(self, quadratic_equation_repository: QuadraticEquationRepository = Depends()) -> None:
        self.__quadratic_equation_repository = quadratic_equation_repository

    async def __solve_with_zero_b(self, value_a: int, value_c: int) -> tuple[float | None]:
        """Решить квадратное уравнения, где b = 0."""
        value = -value_c / value_a
        if value > 0:
            value_x1 = math.sqrt(value)
            return (value_x1, -value_x1)
        return (None, None)

    async def __solve_with_zero_c(self, value_a: int, value_b: int) -> tuple[float | None]:
        """Решить квадратное уравнения, где с = 0."""
        return (-value_b / value_a, 0)

    async def __solve_with_zero_b_and_c(self) -> tuple[int | None]:
        """Решить квадратное уравнения, где b = с = 0."""
        return (0, None)

    async def __solve_default(self, value_a: int, value_b: int, value_c: int) -> tuple[float | None]:
        """Решить квадратное уравнения стандартно."""
        discriminant = value_b ** 2 - 4 * value_a * value_c
        if discriminant < 0:
            return (None, None)
        if discriminant == 0:
            return (-value_b / 2 * value_a, None)
        return ((-value_b - math.sqrt(discriminant)) / 2 * value_a, (-value_b + math.sqrt(discriminant)) / 2 * value_a)

    async def __solve_quadratic_equation(self, value_a: int, value_b: int, value_c: int) -> tuple[float | None]:
        """Решить квадртаное уравнение."""
        if value_b == 0 and value_c != 0:
            return await self.__solve_with_zero_b(value_a, value_c)
        if value_b != 0 and value_c == 0:
            return await self.__solve_with_zero_c(value_a, value_b)
        if value_b == value_c == 0:
            return await self.__solve_with_zero_b_and_c()
        return await self.__solve_default(value_a, value_b, value_c)

    async def create(self, schema: QuadraticEquationCreateRequest) -> QuadraticEquation:
        """Создать квадратное уравнение с решением."""
        value_a, value_b, value_c = (value for value in schema.dict().values())
        value_x1, value_x2 = await self.__solve_quadratic_equation(value_a, value_b, value_c)
        return await self.__quadratic_equation_repository.create(
            QuadraticEquation(
                value_a=value_a,
                value_b=value_b,
                value_c=value_c,
                value_x1=(None if value_x1 is None else round(value_x1, 2)),
                value_x2=(None if value_x2 is None else round(value_x2, 2))
            )
        )

    async def get_all(self, offset: Optional[int] = None, limit: Optional[int] = None) -> list[QuadraticEquation]:
        """Получить список квадратных уравнений с решением."""
        return await self.__quadratic_equation_repository.get_all(offset, limit)
