from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.auth.router import router as auth_router
from src.config import  settings
from src.database import engine,database
from src import models

models.Base.metadata.create_all(bind=engine)
app =FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]

)

@app.on_event("startup")
async def startup() -> None:
    await database.connect()

@app.on_event("shutdown")
async def shutdown() -> None:
    await database.disconnect()

@app.get("/healthcheck", include_in_schema=False)
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
