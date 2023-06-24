import json

from httpx import AsyncClient
from backend.task_one.repository import QuadraticEquationRepository
from backend.task_one.request_schemas import QuadraticEquationCreateRequest
from backend.task_one.service import QuadraticEquationService

from backend.task_two.service import ColoredObjectsService
from tests.conftest import async_session_test

TASK_ONE_URL = "/quadratic_equations/"
TASK_TWO_URL = "/colored_objects/"

TASK_TWO_COLORS = ("BLUE", "GREEN", "RED")
TASK_TWO_RIGHT_DATA = range(1, 100)
TASK_TWO_WRONG_DATA = (-1, 0, 101, "test")
TASK_ONE_WRONG_DATA = {"value_a": 0, "value_b": 5, "value_c": 5}
TASK_ONE_RIGHT_DATA_AND_RESULT = (
    # Случаи, где b = c = 0
    ({"value_a": 10, "value_b": 0, "value_c": 0}, {"value_x1": 0, "value_x2": None}),
    ({"value_a": -5, "value_b": 0, "value_c": 0}, {"value_x1": 0, "value_x2": None}),
    # Случаи, где b = 0
    ({"value_a": 10, "value_b": 0, "value_c": 5}, {"value_x1": None, "value_x2": None}),
    ({"value_a": 5, "value_b": 0, "value_c": -5}, {"value_x1": 1, "value_x2": -1}),
    ({"value_a": -5, "value_b": 0, "value_c": 5}, {"value_x1": 1, "value_x2": -1}),
    # Случаи, где c = 0
    ({"value_a": 10, "value_b": 5, "value_c": 0}, {"value_x1": -0.5, "value_x2": 0}),
    ({"value_a": 5, "value_b": -5, "value_c": 0}, {"value_x1": 1, "value_x2": 0}),
    ({"value_a": -5, "value_b": 5, "value_c": 0}, {"value_x1": 1, "value_x2": 0}),
    # Общие случаи
    ({"value_a": 1, "value_b": 5, "value_c": 1}, {"value_x1": -4.79, "value_x2": -0.21}),
    ({"value_a": 1, "value_b": 4, "value_c": 4}, {"value_x1": -2, "value_x2": None}),
    ({"value_a": 4, "value_b": 4, "value_c": 4}, {"value_x1": None, "value_x2": None})
)

TEXT_ERROR_WRONG_RESULT = "Не правильное решение уравнения. Данные: {data}. Результат: {body}."
TEXT_ERROR_WRONG_COLOR = "Ошибка ответа функции получения цвета: {color}."
TEXT_ERROR_NOT_200 = "Ответ на запрос отличный от 200. Ошибка: {error}."
TEXT_ERROR_NOT_422 = "Ответ на запрос отличный от 422. Ошибка: {error}."


async def test_task_one_api_right_data(async_client: AsyncClient):
    for data, result in TASK_ONE_RIGHT_DATA_AND_RESULT:
        response = await async_client.post(
            url=TASK_ONE_URL,
            data=json.dumps(data),
            headers={"Content-Type": "application/json"}
        )
        body = response.json()
        assert response.status_code == 201, TEXT_ERROR_NOT_200.format(error=body)
        assert body.get("value_x1") == result.get("value_x1"), TEXT_ERROR_WRONG_RESULT.format(data=data, body=body)
        assert body.get("value_x2") == result.get("value_x2"), TEXT_ERROR_WRONG_RESULT.format(data=data, body=body)


async def test_task_one_api_wrong_data(async_client: AsyncClient):
    response = await async_client.post(
        url=TASK_ONE_URL,
        data=json.dumps(TASK_ONE_WRONG_DATA),
        headers={"Content-Type": "application/json"}
    )
    body = response.json()
    assert response.status_code == 422, TEXT_ERROR_NOT_422.format(error=body)


async def test_task_one_api_get_list(async_client: AsyncClient):
    response = await async_client.get(url=TASK_ONE_URL)
    assert response.status_code == 200, TEXT_ERROR_NOT_200.format(error=response.json())


async def test_task_one_service_create() -> None:
    async with async_session_test() as session:
        service = QuadraticEquationService(QuadraticEquationRepository(session))
        for data, result in TASK_ONE_RIGHT_DATA_AND_RESULT:
            decision = await service.create(QuadraticEquationCreateRequest(**data))
            assert decision.value_x1 == result.get("value_x1"), TEXT_ERROR_WRONG_RESULT.format(data=data, body=decision)
            assert decision.value_x2 == result.get("value_x2"), TEXT_ERROR_WRONG_RESULT.format(data=data, body=decision)


async def test_task_two_api_right_data(async_client: AsyncClient):
    for number in TASK_TWO_RIGHT_DATA:
        response = await async_client.get(url=TASK_TWO_URL, params={"number": number})
        body = response.json()
        assert response.status_code == 200, TEXT_ERROR_NOT_200.format(error=body)
        color = body.get("color")
        assert color in TASK_TWO_COLORS, TEXT_ERROR_WRONG_COLOR.format(color=color)


async def test_task_two_api_wrong_data(async_client: AsyncClient):
    for number in TASK_TWO_WRONG_DATA:
        response = await async_client.get(url=TASK_TWO_URL, params={"number": number})
        assert response.status_code == 422, TEXT_ERROR_NOT_422.format(body=response.json())


async def test_task_two_service_choose() -> None:
    service = ColoredObjectsService()
    for number in TASK_TWO_RIGHT_DATA:
        decision = await service.choose(number)
        color = decision.get("color")
        assert color in TASK_TWO_COLORS, TEXT_ERROR_WRONG_COLOR.format(color=color)
