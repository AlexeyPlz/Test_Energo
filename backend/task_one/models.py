from sqlalchemy import Column, Float, Integer

from backend.core.base_models import Base


class QuadraticEquation(Base):
    """Модель квадратного выражения."""

    __tablename__ = "quadratic_equations"

    value_a = Column(Integer, nullable=False)
    value_b = Column(Integer, nullable=False)
    value_c = Column(Integer, nullable=False)
    value_x1 = Column(Float, nullable=True)
    value_x2 = Column(Float, nullable=True)

    def __repr__(self) -> str:
        return (
            f"<QuadraticEquation - ID: {self.id} - A: {self.value_a} - B: {self.value_b} - "
            f"C: {self.value_c} - X1: {self.value_x1} - X2: {self.value_x2}>"
        )
