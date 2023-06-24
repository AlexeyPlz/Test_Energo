from sqlalchemy import TIMESTAMP, Column, Integer, func
from sqlalchemy.ext.declarative import as_declarative


@as_declarative()
class Base:
    """Базовая модель."""

    __name__: str

    id = Column(Integer, primary_key=True)
    created_at = Column(
        TIMESTAMP,
        server_default=func.current_timestamp(),
        nullable=False,
        index=True
    )
    updated_at = Column(
        TIMESTAMP,
        server_default=func.current_timestamp(),
        onupdate=func.current_timestamp(),
        nullable=False,
        index=True
    )
