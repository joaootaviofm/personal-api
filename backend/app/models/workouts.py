from datetime import date
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Workout(Base):
    __tablename__ = "workouts"

    id : Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str]
    trained_on : Mapped[date]
    exercises : Mapped[list[dict]] = mapped_column(JSONB)
