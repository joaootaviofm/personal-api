from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.workouts import Workout 
from app.schemas.workouts import WorkoutCreate

# Create Workout
def create_workout(db : Session, data : WorkoutCreate) -> Workout:
    workout = Workout(
        name=data.name,
        trained_on=data.trained_on,
        exercises=[exercise.model_dump() for exercise in data.exercises]
    )
    db.add(workout)
    db.commit()
    db.refresh(workout)
    return workout

# Delete Workout by Id
def delete_workout(db : Session, workout_id : int) -> bool:
    workout = db.get(Workout, workout_id)
    if workout is None:
        return False
    db.delete(workout)
    db.commit()
    return True


# Get All Workouts 
def get_workouts(db : Session) -> list[Workout]:
    return list(db.scalars(select(Workout)))

def get_workout_by_id(db : Session, workout_id) -> bool:
    workout = db.get(Workout, workout_id)
    if workout is None:
        return False
    
    return workout