from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from backend.core.base_db import get_session
from backend.core.base_repository import AbstractRepository
from backend.task_one.models import QuadraticEquation


class QuadraticEquationRepository(AbstractRepository):
    """Репозиторий для работы с квадртаными выражениями."""

    def __init__(self, session: AsyncSession = Depends(get_session)) -> None:
        super().__init__(session, QuadraticEquation)
