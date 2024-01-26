from sqlalchemy.orm import Session
from database.schemas import ProjetoSchema
from database.model import Projeto
from fastapi import FastAPI
from datetime import datetime
import pytz
import json

def f_get_projeto_all(db:Session, skip: int=0, limit: int = 100):

    _projetos = db.query(Projeto).offset(skip).limit(limit).all()

    projetos_list = []
    for projeto in _projetos:
        projeto_dict = {column.name: getattr(projeto, column.name) for column in Projeto.__table__.columns}
        projetos_list.append(projeto_dict)

    return projetos_list

def f_get_projeto_by_id(db:Session,projeto_id:int):
    return db.query(Projeto).filter(Projeto.id == projeto_id).first()

def f_create_projeto(db:Session, projeto: ProjetoSchema):
    _projeto = Projeto(
        nome= projeto.nome,
        descricao= projeto.descricao,
        data_inicio= projeto.data_inicio,
        data_conclusao_prevista= projeto.data_conclusao_prevista,
        data_conclusao_real= projeto.data_conclusao_real,
        num_desenvolvedores= projeto.num_desenvolvedores,
        horas_desenvolvimento= projeto.horas_desenvolvimento,
        stack= projeto.stack,
        senioridade= projeto.senioridade,
        area= projeto.area,
    )

    db.add(_projeto)
    db.commit()
    db.refresh(_projeto)
    return _projeto

def f_remove_projeto(db:Session, projeto_id: int):
    _projeto = f_get_projeto_by_id(db=db,projeto_id=projeto_id)
    db.delete(_projeto)
    db.commit()

def f_update_projeto(db:Session,projeto_id: int,nome: str,descricao: str,data_inicio: datetime,data_conclusao_prevista: datetime,data_conclusao_real: datetime,num_desenvolvedores: int,horas_desenvolvimento: int,stack: str, senioridade: str, area: str):

    _projeto = f_get_projeto_by_id(db,projeto_id)
    _projeto.nome= nome,
    _projeto.descricao= descricao,
    _projeto.data_inicio= data_inicio,
    _projeto.data_conclusao_prevista= data_conclusao_prevista,
    _projeto.data_conclusao_real= data_conclusao_real,
    _projeto.num_desenvolvedores= num_desenvolvedores,
    _projeto.horas_desenvolvimento= horas_desenvolvimento,
    _projeto.stack= stack,
    _projeto.senioridade= senioridade,
    _projeto.area= area,

    db.commit()

    return _projeto