from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session 
from app.schemas.workouts import WorkoutCreate, WorkoutRead
from app.db.db import get_db
from app.models.workouts import Workout
from app.services.workouts import create_workout
router = APIRouter(prefix="/workouts", tags=["workouts"])

@router.post("/", response_model=WorkoutRead, status_code=201)
def post_workout(data : WorkoutCreate, db : Session = Depends(get_db)) -> Workout:
    return create_workout(db, data)
