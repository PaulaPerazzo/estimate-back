from sqlalchemy.orm import Session
from database.schemas import UsuarioSchema
from database.model import Usuario
from fastapi import FastAPI
from datetime import datetime

router = FastAPI()
#Database

def get_usuario(db:Session, skip: int=0, limit: int = 100):
    return db.query(Usuario).offset(skip).limit(limit).all()

def get_usuario_by_id(db:Session,usuario_id:int):
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()

def create_usuario(db:Session, usuario: UsuarioSchema):
    _usuario = Usuario(
        nome= usuario.nome,
        email= usuario.email,
        senha= usuario.senha,
        experiencia= usuario.experiencia,
        data_cadastro= usuario.data_cadastro,
        tipo= usuario.tipo,
        horas_semanais= usuario.horas_semanais,
        empresa_id= usuario.empresa_id,
        cargo_atual= usuario.cargo_atual,
        nickname= usuario.nickname,
        especialista= usuario.especialista
    )

    db.add(_usuario)
    db.commit()
    db.refresh(_usuario)
    return _usuario

def remove_usuario(db:Session, usuario_id: int):
    _usuario = get_usuario_by_id(db=db,usuario_id=usuario_id)
    db.delete(_usuario)
    db.commit()

def update_usuario(db:Session,usuario_id: int, nome: str,email: str,senha: str,experiencia: str,data_cadastro: datetime,tipo: str,horas_semanais: int,empresa_id: str,cargo_atual: str,nickname: str,especialista: str):
    _usuario = get_usuario_by_id(db=db,usuario_id=usuario_id)
    _usuario.id = usuario_id
    _usuario.nome = nome
    _usuario.email = email
    _usuario.senha = senha
    _usuario.experiencia = experiencia
    _usuario.data_cadastro = data_cadastro
    _usuario.tipo = tipo
    _usuario.horas_semanais = horas_semanais
    _usuario.empresa_id = empresa_id
    _usuario.cargo_atual = cargo_atual
    _usuario.nickname = nickname
    _usuario.especialista = especialista

    db.commit()
    db.refresh()

    return _usuario