from fastapi import FastAPI  # pyright: ignore[reportMissingImports]
from app.routers.health import router as health_router
from app.routers.workouts import router as workouts_router

app = FastAPI()

app.include_router(health_router)
app.include_router(workouts_router)
