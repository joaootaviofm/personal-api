from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.workouts import WorkoutCreate, WorkoutRead
from app.db.db import get_db
from app.models.workouts import Workout
from app.services.workouts import create_workout, delete_workout, get_workout_by_id, get_workouts

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

@router.get("/{workout_id}", response_model=WorkoutRead)
def get_workout_by_id_route(workout_id : int, db : Session = Depends(get_db)):
    
    workout = get_workout_by_id(db, workout_id)
    if workout is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Workout not found."
        )
    return workout 