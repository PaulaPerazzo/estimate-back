# models.py
from typing import List, Optional
from uuid import UUID, uuid4
from enum import Enum

from pydantic import BaseModel
from sqlalchemy import Boolean, Column, Integer, String, DateTime, func, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from database.config import Base

### TABLE user (input model (UserBase) and table columns (User))
class UserBase(BaseModel):
    name: str
    email: str
    password: str
    experience: str
    user_type: int
    week_hours: float
    company_id: int
    current_job: str
    nickname: str
    expert: bool


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
    experience = Column(String(100))
    date_register = Column(DateTime, default=func.now())
    user_type = Column(Integer, nullable=False)
    week_hours = Column(Float)
    current_job = Column(String(100), nullable=False)
    nickname = Column(String(40), unique=True, nullable=False)
    expert = Column(Boolean, nullable=False)
    company_id = Column(Integer, nullable=False)
    projects = relationship("UsuarioProjeto", back_populates="user")
