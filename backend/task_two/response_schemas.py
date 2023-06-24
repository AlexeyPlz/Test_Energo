from backend.core.base_response_schemas import ResponseBase


class ColoredObjectsResponse(ResponseBase):
    """Схема для отображения цвета объекта."""

    color: str
