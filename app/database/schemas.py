from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel,Field
from pydantic.generics import GenericModel
from datetime import datetime

T = TypeVar('T')

class UsuarioSchema(BaseModel):
    id: Optional[int]=None
    nome: str
    email: str
    senha: str
    experiencia: str
    data_cadastro: Optional[datetime] = None
    tipo: str
    horas_semanais: int
    empresa_id: str
    cargo_atual: str
    nickname: str
    especialista: bool

    class Config:
        orm_mode = True

class RequestUsuario(BaseModel):
    nome: str
    email: str
    senha: str
    experiencia: str
    tipo: str
    horas_semanais: int
    empresa_id: str
    cargo_atual: str
    nickname: str
    especialista: bool

class Response (GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]