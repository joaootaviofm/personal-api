from datetime import datetime, timedelta
from decimal import Decimal, ROUND_HALF_UP
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.sleep import Sleep
from app.schemas.sleep import SleepCreate, SleepUpdate

# Compute Total Hours Function
def compute_total_hours(slept_on, bedtime, wakeup_time) -> Decimal:
    start = datetime.combine(slept_on, bedtime) # 2026-11-07 23:30
    end = datetime.combine(slept_on, wakeup_time) # 2026-11-07 07:00
    if end <= start:
        end += timedelta(days=1) # 2026-11-08 07:00
    hours = Decimal((end - start).total_seconds()) / Decimal(3600)
    return hours.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

# POST Service
def create_sleep(db: Session, data: SleepCreate) -> Sleep:
    sleep = Sleep(
        slept_on=data.slept_on,
        bedtime=data.bedtime,
        wakeup_time=data.wakeup_time,
        total_hours=compute_total_hours(data.slept_on, data.bedtime, data.wakeup_time),
        quality=data.quality,
    )
    db.add(sleep)
    db.commit()
    db.refresh(sleep)
    return sleep

# GET All Service
def get_sleeps(db : Session) -> list[Sleep]:
    return list(db.scalars(select(Sleep)))


# GET By Id Service
def get_sleep_by_id(db : Session, sleep_id : int) -> Sleep | None:
    return db.get(Sleep, sleep_id)

# PUT Service
def update_sleep(db : Session, sleep_id : int, data : SleepUpdate) -> Sleep | None:
    sleep = get_sleep_by_id(db, sleep_id)
    if sleep is None:
        return None
    sleep.slept_on = data.slept_on
    sleep.bedtime = data.bedtime
    sleep.wakeup_time = data.wakeup_time
    sleep.quality = data.quality
    sleep.total_hours = compute_total_hours(data.slept_on, data.bedtime, data.wakeup_time)
    db.commit()
    db.refresh(sleep)
    return sleep 



