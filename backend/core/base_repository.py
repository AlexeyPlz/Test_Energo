import abc
from typing import Optional, TypeVar

from sqlalchemy import desc, select
from sqlalchemy.ext.asyncio import AsyncSession

DatabaseModel = TypeVar("DatabaseModel")


class AbstractRepository(abc.ABC):
    """Абстрактный класс репозитория."""

    def __init__(self, session: AsyncSession, model: DatabaseModel) -> None:
        self._session = session
        self._model = model

    async def get_all(self, offset: Optional[int] = None, limit: Optional[int] = None) -> list[DatabaseModel]:
        """Получить список объектов."""
        objects = await self._session.execute(
            select(self._model)
            .order_by(desc(self._model.created_at))
            .offset(offset or 0)
            .limit(limit or 100)
        )
        return objects.scalars().all()

    async def create(self, instance: DatabaseModel) -> DatabaseModel:
        """Создать объект."""
        self._session.add(instance)
        await self._session.commit()
        await self._session.refresh(instance)
        return instance
