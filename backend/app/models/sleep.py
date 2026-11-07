from datetime import date, time
from decimal import Decimal
from sqlalchemy import CheckConstraint, Numeric
from sqlalchemy.orm import Mapped, mapped_column 
from app.models.workouts import Base 

 ## O que é base?
class Sleep(Base):
    __tablename__ = "sleep" 
    __table_args__ = (
        CheckConstraint("quality >= 0 AND quality <= 10", name="quality_betweeen_10_and_10")
    )

    id : Mapped[int] = mapped_column(primary_key=True)
    slept_on : Mapped[date] = mapped_column(unique=True)
    bed_time : Mapped[time]
    wakeup_time : Mapped[time] 
    total_hours : Mapped[Decimal] = mapped_column(Numeric(4,2))
    quality : Mapped[int]