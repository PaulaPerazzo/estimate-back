from fastapi import APIRouter
from typing import List
from uuid import uuid4
from models import Gender, Role, User, UpdateUser, Project
from fastapi import HTTPException
from uuid import UUID

router = APIRouter()
#Database

table_project: List[Project] = [
    Project(
        id=uuid4(),
        nome="Tela de Login",
        descricao= "Teste de descrição",
        data_inicio= "2024-01-16",
        data_conclusao_prevista= "2024-10-05",
        data_conclusao_real= "2024-12-06",
        num_desenvolvedores= 10,
        horas_desenvolvimento= 800,
        gargalos= "Tecnologia, Horário",
        palavras_chave= "Login, Tela, Desenvolvimento, Frontend",
        empresa_id = '2'
    )
]

#GET ALL
@router.get("/projects")
async def get_projects():
    return table_project

#GET BY ID
@router.get("/projects/{id}")
async def get_project(id: UUID):
    for project in table_project:
        if project.id == id:
            return project
    raise HTTPException(status_code=404, detail=f"Não foi possivel achar usuário com o id: {id}")

#CREATE

@router.post("/projects")
async def create_project(project: Project):
    table_project.append(project)
    return {"detail": f"Usuário criado! id: {project.id}"}

#UPDATE

@router.put("/projects/{id}")
async def update_project(project_update: Project, id: UUID):
    for project in table_project:
        if project.id == id:
            if project_update.nome is not None:
                project.nome = project_update.nome
            if project_update.descricao is not None:
                project.descricao = project_update.descricao
            if project_update.data_inicio is not None:
                project.data_inicio = project_update.data_inicio
            if project_update.data_conclusao_prevista is not None:
                project.data_conclusao_prevista = project_update.data_conclusao_prevista
            if project_update.data_conclusao_real is not None:
                project.data_conclusao_real = project_update.data_conclusao_real
            if project_update.num_desenvolvedores is not None:
                project.num_desenvolvedores = project_update.num_desenvolvedores
            if project_update.gargalos is not None:
                project.gargalos = project_update.gargalos
            if project_update.palavras_chave is not None:
                project.palavras_chave = project_update.palavras_chave
            if project_update.empresa_id is not None:
                project.empresa_id = project_update.empresa_id

            return {'detail': 'Projeto atualizado!'}

    raise HTTPException(status_code=404, detail=f"Não foi encontrado usuário com ID: {id}")

#DELETE

@router.delete("/projects/{id}")
async def delete_project(id: UUID):
    for user in table_project:
        if user.id == id:
            table_project.remove(user)
        return
    raise HTTPException(
        status_code=404, detail=f"Delete user failed, id {id} not found.")