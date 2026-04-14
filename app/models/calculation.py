from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class Calculation(Base):
    __tablename__ = "calculations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    a: Mapped[float] = mapped_column(Float, nullable=False)
    b: Mapped[float] = mapped_column(Float, nullable=False)
    type: Mapped[str] = mapped_column(String(20), nullable=False)
    result: Mapped[float] = mapped_column(Float, nullable=False)
