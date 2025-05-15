from fastapi import FastAPI
from auth import router as auth_router
import models
from database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router, prefix="/auth")

