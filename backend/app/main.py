from fastapi import FastAPI
from app.routers.health import router as health_router
from app.routers.workouts import router as workouts_router
from app.core.settings import settings
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_origin],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(workouts_router)
