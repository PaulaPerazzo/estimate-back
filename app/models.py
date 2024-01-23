# models.py
from typing import List, Optional
from uuid import UUID, uuid4
from enum import Enum
from database.config import Base
from pydantic import BaseModel
from sqlalchemy import Boolean, Column, Integer, String

class UserBase(BaseModel):
    username: str

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True)


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), unique=False)
    description = Column(String(100), unique=False)

class Links(Base):
    __tablename__ = 'links'

    id = Column(Integer, primary_key=True, index=True)
    link = Column(String(50), unique=False)
    description = Column(String(100), unique=False)
