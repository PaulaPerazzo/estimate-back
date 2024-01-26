from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func
from database.config import Base

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
    cargo_atual = Column(String)
    nickname = Column(String)
    especialista = Column(Boolean)

class Usuario_Projeto(Base):
    __tablename__ = 'usuario_projeto'

    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer)
    projeto_id = Column(Integer)

class Projeto(Base):
    __tablename__ = 'projeto'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    descricao = Column(String)
    data_inicio = Column(DateTime(timezone=True))
    data_conclusao_prevista = Column(DateTime(timezone=True))
    data_conclusao_real = Column(DateTime(timezone=True))
    num_desenvolvedores = Column(Integer)
    horas_desenvolvimento = Column(Integer)
    stack = Column(String)
    senioridade = Column(String)
    area = Column(String)

class Avaliacao(Base):
    __tablename__ = 'avaliacao'

    id = Column(Integer, primary_key=True, autoincrement=True)
    avaliacao = Column(String)
    usuario_id = Column(Integer)
    atividade_id = Column(Integer)

class Atividade(Base):
    __tablename__ = 'atividade'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    descricao = Column(String)
    data_inicio = Column(DateTime(timezone=True))
    data_conclusao_prevista = Column(DateTime(timezone=True))
    data_conclusao_real = Column(DateTime(timezone=True))
    horas_estimadas = Column(Integer)
    horas_desenvolvimento = Column(Integer)
    gargalos = Column(String)
    palavras_chave = Column(String)
    projeto_id = Column(Integer)
    requisitos = Column(String)
    framework = Column(String)
    biblioteca = Column(String)
    usuario_id = Column(Integer)
    sugestao = Column(String)
    acao = Column(String)



