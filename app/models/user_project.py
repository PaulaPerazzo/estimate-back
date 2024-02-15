from sqlalchemy import Column, Integer, ForeignKey, Table
from database.config import Base

# models.py
from typing import List, Optional
from uuid import UUID, uuid4
from enum import Enum

from pydantic import BaseModel
from sqlalchemy import Boolean, Column, Integer, String, DateTime, func, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from database.config import Base

class UsuarioProjeto(Base):
    __tablename__ = "usuario_projeto"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    project_id = Column(Integer, ForeignKey("projects.id", ondelete="CASCADE"))
    
    user = relationship("User", back_populates="projects")
    project = relationship("Project", back_populates="users")
