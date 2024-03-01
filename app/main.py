from typing import Callable
from database.config import SessionLocal
from fastapi import FastAPI, Depends, status, HTTPException
from os import environ as env
from fastapi.middleware.cors import CORSMiddleware
from models.user import User, UserBase
from models.project import ProjectBase, Project
from models.task import TaskBase, Task
from models.valuation import ValuationBase, Valuation
from models.user_project import UsuarioProjeto

from sqlalchemy.orm import Session

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3306",
    "http://localhost:3307",
    "http://localhost:3000",
    "https://estimate-dev.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_headers=["*"],
    allow_methods=["*"],
    allow_credentials=True,
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
async def create_project(project: ProjectBase, user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db_project = Project(**project.dict())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)

    project_object = Project
    print(project_object)
    user_project_association = UsuarioProjeto(user_id=user_id, project_id=db_project.id)
    db.add(user_project_association)
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


@app.get("/project/userProject/{user_id}", status_code=status.HTTP_200_OK, tags=["Projetos"])
async def read_user_projects(user_id: int, db: Session = Depends(get_db)):
    project = db.query(UsuarioProjeto).filter(UsuarioProjeto.user_id == user_id).all()

    if project is None:
        raise HTTPException(status_code=404, detail="Projects not found for this user")
    
    projects_data: List[dict] = []

    for value in project:
        projects_data.append({
            'id': value.id,
            'user': value.user,
            'project': value.project
        })

    return projects_data


### CRUD tasks ###
@app.post("/task/", status_code=status.HTTP_201_CREATED, tags=["Atividades"])
async def create_task(task: TaskBase, db: Session = Depends(get_db)):
    db_task = Task(**task.dict())
    db.add(db_task)
    db.commit()

    return task


@app.get("/task/", status_code=status.HTTP_200_OK, tags=["Atividades"])
async def read_task(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    tasks = db.query(Task).offset(skip).limit(limit).all()
    return tasks


@app.get("/task/{task_id}", status_code=status.HTTP_200_OK, tags=["Atividades"])
async def read_task_by_id(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    user = task.user.name if task.user else "Unknown"
    
    public_task = {
        'id': task.id,
        'task_action': task.task_action,
        'created_by': user,
        'component_action': task.component_task
    }

    return public_task


@app.get("/task-info/{task_id}", status_code=status.HTTP_200_OK, tags=["Atividades"])
async def read_task_by_id(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    user = task.user.name if task.user else "Unknown"
    
    task_info = {
        **task.__dict__,
        'created_by': user
    }

    return task_info


@app.put("/task/{task_id}", status_code=status.HTTP_200_OK, tags=["Atividades"])
async def update_task(
    task_id: int, update_task: TaskBase, db: Session = Depends(get_db)
):
    task = db.query(Task).filter(Task.id == task_id).first()

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    for key, value in update_task.dict().items():
        setattr(task, key, value)

    db.commit()

    return update_task


@app.delete("/task/{task_id}", status_code=status.HTTP_200_OK, tags=["Atividades"])
async def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()

    return {"message": "project deleted"}


@app.get("/task/projectTask/{project_id}", status_code=status.HTTP_200_OK, tags=["Atividades"])
async def read_task_by_project(project_id: int, db: Session = Depends(get_db)):
    tasks = db.query(Task).filter(Task.project_id == project_id).all()

    if tasks is None:
        raise HTTPException(status_code=404, detail="Tasks not found for this project")
    
    tasks_data = []

    for task in tasks:
        tasks_data.append({
            **task.__dict__,
            'project': task.project
        })

    return tasks_data


### CRUD valuations ###
@app.post("/valuation/", status_code=status.HTTP_201_CREATED, tags=["Avaliações"])
async def create_valuation(valuation: ValuationBase, db: Session = Depends(get_db)):
    db_valuation = Valuation(**valuation.dict())
    db.add(db_valuation)
    db.commit()

    return valuation


@app.get("/valuation/", status_code=status.HTTP_200_OK, tags=["Avaliações"])
async def read_valuation(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    valuation = db.query(Valuation).offset(skip).limit(limit).all()
    return valuation


@app.get("/valuation/{valuation_id}", status_code=status.HTTP_200_OK, tags=["Avaliações"])
async def read_valuation_by_id(valuation_id: int, db: Session = Depends(get_db)):
    valuation = db.query(Valuation).filter(Valuation.id == valuation_id).first()

    if valuation is None:
        raise HTTPException(status_code=404, detail="Valuation not found")

    return valuation

@app.get("/valuation/task-comments/{task_id}", status_code=status.HTTP_200_OK, tags=["Avaliações"])
async def read_all_task_valuations(task_id: int, db: Session = Depends(get_db)):
    valuation = db.query(Valuation).filter(Valuation.task_id == task_id).all()

    if valuation is None:
        raise HTTPException(status_code=404, detail="Valuation not found")
    
    comments_data: List[dict] = []

    for value in valuation:
        comments_data.append({
            'id': value.id,
            'user': value.user,
            'task': value.task,
            'comment': value.valuation,
        })

    return comments_data


@app.put("/valuation/{valuation_id}", status_code=status.HTTP_200_OK, tags=["Avaliações"])
async def update_valuation(
    valuation_id: int, update_valuation: ValuationBase, db: Session = Depends(get_db)
):
    valuation = db.query(Valuation).filter(Valuation.id == valuation_id).first()

    if valuation is None:
        raise HTTPException(status_code=404, detail="Valuation not found")

    for key, value in update_valuation.dict().items():
        setattr(valuation, key, value)

    db.commit()

    return update_valuation


@app.delete("/valuation/{valuation_id}", status_code=status.HTTP_200_OK, tags=["Avaliações"])
async def delete_valuation(valuation_id: int, db: Session = Depends(get_db)):
    valuation = db.query(Valuation).filter(Valuation.id == valuation_id).first()

    if valuation is None:
        raise HTTPException(status_code=404, detail="Valuation not found")

    db.delete(valuation)
    db.commit()

    return {"message": "valuation deleted"}
