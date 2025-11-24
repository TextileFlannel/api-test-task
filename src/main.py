from fastapi import FastAPI
from src.routers import handlers
from src.database import engine
import src.models

src.models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(handlers.router)