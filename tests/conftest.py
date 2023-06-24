import asyncio
from typing import AsyncGenerator

import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

try:
    from backend.application import create_app
except (NameError, ImportError):
    raise AssertionError(
        "Не удалось импортировать метод 'create_app'."
        "Подсказка: метод должен быть доступен в модуле 'backend.application'.",
    )

try:
    from backend.task_one.models import QuadraticEquation
except (NameError, ImportError):
    raise AssertionError(
        "Не удалось импортировать объект 'QuadraticEquation'."
        "Подсказка: объект должен быть доступен в модуле 'backend.task_one.models'.",
    )


try:
    from backend.core.base_db import get_session
except (NameError, ImportError):
    raise AssertionError(
        "Не удалось импортировать метод 'get_session'."
        "Подсказка: метод должен быть доступен в модуле 'backend.core.base_db'.",
    )


engine_test = create_async_engine("sqlite+aiosqlite:///test_db", connect_args={"check_same_thread": False})
async_session_test = sessionmaker(bind=engine_test, class_=AsyncSession, autocommit=False, autoflush=False)


async def override_get_session() -> AsyncGenerator[AsyncSession, None]:
    """Создание зависимости для тестовой БД."""
    async with async_session_test() as session:
        yield session


@pytest.fixture(autouse=True, scope='session')
async def prepare_database():
    """Создание тестовой БД в начале тестирования."""
    async with engine_test.begin() as connection:
        await connection.run_sync(QuadraticEquation.metadata.create_all)
    yield
    """Удаление тестовой БД в конце тестирования."""
    async with engine_test.begin() as connection:
        await connection.run_sync(QuadraticEquation.metadata.drop_all)


@pytest.fixture(scope='session')
def event_loop(request):
    """Создание экземпляра цикла событий по умолчанию для каждого тестового случая."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope='session')
async def async_client() -> AsyncGenerator[AsyncClient, None]:
    """Создание асинхронного клиента."""
    app = create_app()
    app.dependency_overrides[get_session] = override_get_session
    async with AsyncClient(app=app, base_url="http://test") as async_client:
        yield async_client
