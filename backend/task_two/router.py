from http import HTTPStatus

from fastapi import APIRouter, Depends, Query
from fastapi_restful.cbv import cbv

from backend.task_two.response_schemas import ColoredObjectsResponse
from backend.task_two.service import ColoredObjectsService

router = APIRouter(prefix="/colored_objects", tags=["ColoredObjects"])


@cbv(router)
class ColoredObjectsCBV:
    """CBV для работы с цветными объектами."""

    __сolored_objects_service: ColoredObjectsService = Depends()

    @router.get(
        '/',
        response_model=ColoredObjectsResponse,
        status_code=HTTPStatus.OK,
        summary="Получить цвет объекта из группы."
    )
    async def choose(self, number: int = Query(ge=1, le=100)) -> ColoredObjectsResponse:
        """
        Поля для получения цвета объекта из группы в 100 объектов.

        - **number**: номер объекта в группе

        """
        return await self. __сolored_objects_service.choose(number)
