from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from starlette.status import HTTP_404_NOT_FOUND 
from app.schemas.workouts import WorkoutCreate, WorkoutRead
from app.db.db import get_db
from app.models.workouts import Workout
from app.services.workouts import create_workout, delete_workout, get_workouts

router = APIRouter(prefix="/workouts", tags=["workouts"])

@router.post("/", response_model=WorkoutRead, status_code=201)
def post_workout(data : WorkoutCreate, db : Session = Depends(get_db)) -> Workout:
    return create_workout(db, data)

@router.delete("/{workout_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_workout_route(workout_id : int, db : Session = Depends(get_db)) -> None:
    deleted = delete_workout(db, workout_id)
    if not deleted:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail="Workout not found."
        )
    
@router.get("/", response_model=list[WorkoutRead])
def get_workouts_route(db : Session = Depends(get_db)):
    return get_workouts(db)