from fastapi import APIRouter, Depends, status, HTTPException
from app.db.db import get_db
from sqlalchemy.orm import Session 
from app.core.auth import require_api_token
from app.schemas.sleep import SleepCreate, SleepRead, SleepUpdate
from app.services.sleep import create_sleep, get_sleeps, get_sleep_by_id, update_sleep

router = APIRouter(prefix="/sleep", tags=["sleep"], dependencies=[Depends(require_api_token)])

# Create Sleep Route
@router.post("/", response_model=SleepRead, status_code=status.HTTP_201_CREATED)
def create_sleep_route(data : SleepCreate, db : Session = Depends(get_db)):
    return create_sleep(db, data)

# Get All Sleeps Route
@router.get("/", response_model=list[SleepRead], status_code=status.HTTP_200_OK)
def get_sleeps_route(db : Session = Depends(get_db)):
    return get_sleeps(db)


# Get Sleeps By Id Route
@router.get("/{sleep_id}", response_model=SleepRead, status_code=status.HTTP_200_OK)
def get_sleep_by_id_route(sleep_id : int, db : Session = Depends(get_db)):
    sleep = get_sleep_by_id(db, sleep_id)
    if sleep is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail="Sleep not found."
        )
    return sleep
    

# Update Sleep Route
@router.put("/update/{sleep_id}", response_model=SleepRead, status_code=status.HTTP_200_OK)
def update_sleep_route(sleep_id : int, data: SleepUpdate, db : Session = Depends(get_db)):
    sleep = update_sleep(db, sleep_id, data)
    if sleep is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sleep not found"
        )
    return sleep


