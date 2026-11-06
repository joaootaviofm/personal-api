from datetime import date
from pydantic import BaseModel


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
