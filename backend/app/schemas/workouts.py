from datetime import date
from pydantic import BaseModel, ConfigDict


class Set(BaseModel):
    weight : float
    repetitions : float

class Exercise(BaseModel):
    name : str
    sets : list[Set]

class WorkoutCreate(BaseModel):
    name : str
    trained_on : date
    exercises : list[Exercise]

class WorkoutRead(BaseModel):
    id : int
    name: str
    trained_on : date
    exercises : list[Exercise]

    model_config = ConfigDict(from_attributes=True)
