from fastapi import APIRouter
from typing import List
from uuid import uuid4
from models import Gender, Role, User, UpdateUser
from fastapi import HTTPException
from uuid import UUID

router = APIRouter()
#Database

db: List[User] = [
    User(
        id=uuid4(),
        first_name="John",
        last_name="Doe",
        gender=Gender.male,
        roles=[Role.business],
    ),
    User(
        id=uuid4(),
        first_name="Jane",
        last_name="Doe",
        gender=Gender.female,
        roles=[Role.business],
    ),
    User(
        id=uuid4(),
        first_name="James",
        last_name="Gabriel",
        gender=Gender.male,
        roles=[Role.business],
    ),
    User(
        id=uuid4(),
        first_name="Eunit",
        last_name="Eunit",
        gender=Gender.male,
        roles=[Role.admin, Role.dev],
    ),
]


#GET ALL
@router.get("/users")
async def get_users():
    return db

#GET BY ID
@router.get("/users/{id}")
async def read_user(id: UUID):
    for user in db:
        if user.id == id:
            return user
    raise HTTPException(status_code=404, detail=f"Não foi possivel achar usuário com o id: {id}")

#CREATE

@router.post("/users")
async def create_user(user: User):
    db.append(user)
    return {"detail": f"Usuário criado! id: {user.id}"}

#UPDATE

@router.put("/users/{id}")
async def update_user(user_update: UpdateUser, id: UUID):
    for user in db:
        if user.id == id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
        if user_update.last_name is not None:
            user.last_name = user_update.last_name
        if user_update.roles is not None:
            user.roles = user_update.roles
        return user.id
    raise HTTPException(status_code=404, detail=f"Não foi encontrado usuário com ID: {id}")

#DELETE

@router.delete("/users/{id}")
async def delete_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
        return
    raise HTTPException(
        status_code=404, detail=f"Delete user failed, id {id} not found."
    )