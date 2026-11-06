from sqlalchemy.orm import Session

from app.models.workouts import Workout 
from app.schemas.workouts import WorkoutCreate


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

