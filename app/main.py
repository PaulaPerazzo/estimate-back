from typing import Callable
from database.config import SessionLocal
from fastapi import FastAPI, Depends, status, HTTPException
from routers.user import db_dependency
from os import environ as env
from fastapi.middleware.cors import CORSMiddleware
from models.user import User, UserBase
from models.project import ProjectBase, Project
from models.task import TaskBase, Task

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
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()

    return user


@app.get("/user/", status_code=status.HTTP_200_OK, tags=["Usuários"])
async def read_user(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = db.query(User).offset(skip).limit(limit).all()
    return users


@app.get("/user/{user_id}", status_code=status.HTTP_200_OK, tags=["Usuários"])
async def read_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user


@app.put("/user/{user_id}", status_code=status.HTTP_200_OK, tags=["Usuários"])
async def update_user(
    user_id: int, update_user: UserBase, db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    for key, value in update_user.dict().items():
        setattr(user, key, value)

    db.commit()

    return update_user


@app.delete("/user/{user_id}", status_code=status.HTTP_200_OK, tags=["Usuários"])
async def read_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()

    return {"message": "user deleted"}


### CRUD project ###
@app.post("/project/", status_code=status.HTTP_201_CREATED, tags=["Projetos"])
async def create_project(project: ProjectBase, db: Session = Depends(get_db)):
    db_project = Project(**project.dict())
    db.add(db_project)
    db.commit()

    return project


@app.get("/project/", status_code=status.HTTP_200_OK, tags=["Projetos"])
async def read_project(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    projects = db.query(Project).offset(skip).limit(limit).all()
    return projects


@app.get("/project/{project_id}", status_code=status.HTTP_200_OK, tags=["Projetos"])
async def read_project_by_id(project_id: int, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id).first()

    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")

    return project


@app.put("/project/{project_id}", status_code=status.HTTP_200_OK, tags=["Projetos"])
async def update_project(
    project_id: int, update_project: ProjectBase, db: Session = Depends(get_db)
):
    project = db.query(Project).filter(Project.id == project_id).first()

    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")

    for key, value in update_project.dict().items():
        setattr(project, key, value)

    db.commit()

    return update_project


@app.delete("/project/{project_id}", status_code=status.HTTP_200_OK, tags=["Projetos"])
async def delete_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id).first()

    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")

    db.delete(project)
    db.commit()

    return {"message": "project deleted"}
