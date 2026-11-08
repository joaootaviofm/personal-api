from datetime import date, time
from decimal import Decimal
from pydantic import BaseModel, ConfigDict, Field

class SleepCreate(BaseModel): 
    slept_on : date
    bedtime : time
    wakeup_time : time
    quality : int = Field(ge=0, le=10)

class SleepRead(BaseModel):
    id : int
    slept_on : date
    bedtime : time
    wakeup_time : time
    total_hours : Decimal
    quality : int

    model_config = ConfigDict(from_attributes=True)
    

class SleepUpdate(SleepCreate):
    pass 


