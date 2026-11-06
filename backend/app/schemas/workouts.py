from datetime import date
from pydantic import BaseModel

class Exercise(BaseModel):
    name : str
    weight : float
    repetitions : float

class WorkoutCreate(BaseModel):
    name : str
    trained_on : date
    exercises : list[Exercise]
