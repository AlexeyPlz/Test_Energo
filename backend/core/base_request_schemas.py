from pydantic import BaseModel, Extra


class RequestBase(BaseModel):
    """Базовый класс для моделей запросов."""

    class Config:
        extra = Extra.forbid
