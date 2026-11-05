from fastapi import FastAPI  # pyright: ignore[reportMissingImports]
from app.routers.health import router as health_router


app = FastAPI()

app.include_router(health_router)

