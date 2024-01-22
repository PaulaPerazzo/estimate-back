from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func
from config import Base

#Entidades

class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    email = Column(String)
    senha = Column(String)
    experiencia = Column(String)
    data_cadastro = Column(DateTime(timezone=True), default=func.now())
    tipo = Column(String)
    horas_semanais = Column(Integer)
    empresa_id = Column(String)
    cargo_atual = Column(String)
    nickname = Column(String)
    especialista = Column()
    ativo = Column(Boolean, default=True)

class Usuario_Projeto(Base):
    __tablename__ = 'usuario_projeto'

    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer)
    projeto_id = Column(Integer)
