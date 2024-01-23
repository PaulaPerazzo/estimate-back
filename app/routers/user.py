import models
from database.config import SessionLocal
from typing import Callable, List
from sqlalchemy.orm import Session
from fastapi import FastAPI, HTTPException, Depends, status, APIRouter
from models import UserBase
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

@router.post("/users/", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserBase, db: db_dependency):
    db_user = models.User(**user.model_dump())
    db.add(db_user)
    db.commit()


@app.get("/users/{user_id}", status_code=status.HTTP_200_OK)
async def read_user(user_id: int, db: db_dependency):
    user = db.query(models.User).filter(models.User.id == user_id).first()

    if user is None:
        raise HTTPException(status_code=404, detail='User not found')
    
    return user
