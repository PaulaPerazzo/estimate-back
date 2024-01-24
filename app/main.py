from typing import Callable
from database.config import SessionLocal
from fastapi import FastAPI, Depends, status, HTTPException
from routers.user import db_dependency
from os import environ as env
from fastapi.middleware.cors import CORSMiddleware
import models
from models import UserBase
from sqlalchemy.orm import Session

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3306",
    "http://localhost:3307",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir Rotas
# app.include_router(user.router, tags=["User"])
# app.include_router(project.router, tags=["Project"])
# app.include_router(admin.router,tags=["Admin"])


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


def db_dependency(get_db: Callable[[], Session] = Depends(get_db)):
    return get_db()


# Get da Main
@app.get("/", tags=["Main"])
async def root():
    return {"message": f"V1.0.1 API EstiMate"}


### CRUD user ###
@app.post("/user/", status_code=status.HTTP_201_CREATED, tags=["Usuários"])
async def create_user(user: UserBase, db: Session = Depends(get_db)):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()

    return user


@app.get("/user/", status_code=status.HTTP_200_OK, tags=["Usuários"])
async def read_user(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = db.query(models.User).offset(skip).limit(limit).all()
    return users


@app.get("/user/{user_id}", status_code=status.HTTP_200_OK, tags=["Usuários"])
async def read_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user


@app.put("/user/{user_id}", status_code=status.HTTP_200_OK, tags=["Usuários"])
async def update_user(
    user_id: int, update_user: models.UserBase, db: Session = Depends(get_db)
):
    user = db.query(models.User).filter(models.User.id == user_id).first()

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    for key, value in update_user.dict().items():
        setattr(user, key, value)

    db.commit()

    return update_user


@app.delete("/user/{user_id}", status_code=status.HTTP_200_OK, tags=["Usuários"])
async def read_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()

    return {"message": "user deleted"}
