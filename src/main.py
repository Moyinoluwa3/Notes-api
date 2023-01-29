from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.auth.router import router as auth_router
from src.config import app_configs, settings
from src.database import database,engine
from src import models

models.Base.metadata.create_all(bind=engine)
app =FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_origin_regex=settings.CORS_ORIGINS_REGEX,
    allow_credentials=True,
    allow_methods=("GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"),
    allow_headers=settings.CORS_HEADERS,
)
@app.on_event("startup")
async def startup() -> None:
    await database.connect()

@app.on_event("shutdown")
async def shutdown() -> None:
    await database.disconnect()

app.include_router(auth_router, prefix="/auth", tags=["Auth"])