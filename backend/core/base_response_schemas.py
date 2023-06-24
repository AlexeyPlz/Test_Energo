from pydantic import BaseModel


class ResponseBase(BaseModel):
    """Базовый класс для моделей ответов."""

    class Config:
        orm_mode = True
