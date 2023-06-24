from http import HTTPStatus
from typing import Optional

from fastapi import APIRouter, Depends
from fastapi_restful.cbv import cbv

from backend.task_one.request_schemas import QuadraticEquationCreateRequest
from backend.task_one.response_schemas import QuadraticEquationResponse
from backend.task_one.service import QuadraticEquationService

router = APIRouter(prefix="/quadratic_equations", tags=["QuadraticEquation"])


@cbv(router)
class QuadraticEquationCBV:
    """CBV для работы с квадратными выражениями."""

    __quadratic_equation_service: QuadraticEquationService = Depends()

    @router.post(
        '/',
        response_model=QuadraticEquationResponse,
        status_code=HTTPStatus.CREATED,
        summary="Создать квадратное уравнение для решения."
    )
    async def create(self, schema: QuadraticEquationCreateRequest) -> QuadraticEquationResponse:
        """
        Поля для создания квадратного уравнения с решением.

        - **value_a**: Значение A
        - **value_b**: Значение B
        - **value_c**: Значение C
        """
        return await self.__quadratic_equation_service.create(schema)

    @router.get(
        '/',
        response_model=list[QuadraticEquationResponse],
        status_code=HTTPStatus.OK,
        summary="Получить список квадратных уравнений с решением."
    )
    async def get_all(
        self,
        offset: Optional[int] = None,
        limit: Optional[int] = None
    ) -> list[QuadraticEquationResponse]:
        return await self.__quadratic_equation_service.get_all(offset, limit)
