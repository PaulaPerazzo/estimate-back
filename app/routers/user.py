import models.user as models
from database.config import SessionLocal
from typing import Callable, List
from sqlalchemy.orm import Session
from fastapi import FastAPI, HTTPException, Depends, status, APIRouter
from database.config import engine

models.Base.metadata.create_all(bind=engine)
#Database
router = APIRouter()

app = FastAPI()

def get_db():
    db = SessionLocal()
    
    try:
        yield db
    finally:
        db.close()


def db_dependency(get_db: Callable[[], Session] = Depends(get_db)):
    return get_db()
