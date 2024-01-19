# models.py
from typing import List, Optional
from uuid import UUID, uuid4
from enum import Enum
from pydantic import BaseModel

class Gender(str, Enum):
    male = "Masculino"
    female = "Feminino"
class Role(str, Enum):
    admin = "Admin"
    dev = "Dev"
    business = "Business"

#Usuario

class UpdateUser(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    roles: Optional[List[Role]]

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    gender: Gender
    roles: List[Role]

#Projeto

class Project(BaseModel):
    id: Optional[UUID] = uuid4()
    nome: str
    descricao: str
    data_inicio: str
    data_conclusao_prevista: str
    data_conclusao_real: str
    num_desenvolvedores: int
    horas_desenvolvimento: int
    gargalos: str
    palavras_chave: str
    empresa_id: str