from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel,Field
from pydantic.generics import GenericModel
from datetime import datetime

T = TypeVar('T')
class Response (GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
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

    def from_orm(cls, usuario):
        return cls(**usuario.__dict__)
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


class ProjetoSchema(BaseModel):
    id: Optional[int]=None
    nome: str
    descricao: str
    data_inicio: datetime
    data_conclusao_prevista: datetime
    data_conclusao_real: datetime
    num_desenvolvedores: int
    horas_desenvolvimento: int
    stack: str
    senioridade: str
    area: str

    def from_orm(cls, projeto):
        return cls(**projeto.__dict__)
    class Config:
        orm_mode = True

class RequestProjeto(BaseModel):
    nome: str
    descricao: str
    data_inicio: datetime
    data_conclusao_prevista: datetime
    data_conclusao_real: datetime
    num_desenvolvedores: int
    horas_desenvolvimento: int
    stack: str
    senioridade: str
    area: str


class AvaliacaoSchema(BaseModel):
    id: Optional[int]=None
    nome: Optional[str]=None
    usuario_id: Optional[int]=None
    atividade_id: Optional[int]=None

    def from_orm(cls, avaliacao):
        return cls(**avaliacao.__dict__)
    class Config:
        orm_mode = True

class RequestAvaliacao(BaseModel):
    nome: Optional[str]=None
    usuario_id: Optional[int]=None
    atividade_id: Optional[int]=None

class AtividadeSchema(BaseModel):
    id: Optional[int]=None
    nome: str
    descricao: str
    data_inicio: datetime
    data_conclusao_prevista: datetime
    data_conclusao_real: datetime
    horas_estimadas: int
    horas_desenvolvimento: int
    gargalos: str
    palavras_chave: str
    projeto_id: int
    requisitos: str
    framework: str
    biblioteca: str
    usuario_id: int
    sugestao: str
    acao: str


    def from_orm(cls,atividade):
        return cls(**atividade.__dict__)
    class Config:
        orm_mode = True

class RequestAtividade(BaseModel):
    nome: str
    descricao: str
    data_inicio: datetime
    data_conclusao_prevista: datetime
    data_conclusao_real: datetime
    horas_estimadas: int
    horas_desenvolvimento: int
    gargalos: str
    palavras_chave: str
    projeto_id: int
    requisitos: str
    framework: str
    biblioteca: str
    usuario_id: int
    sugestao: str
    acao: str