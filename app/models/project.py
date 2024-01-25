# models.py
from typing import List, Optional
from uuid import UUID, uuid4
from enum import Enum

from pydantic import BaseModel
from sqlalchemy import Boolean, Column, Integer, String, DateTime, func, Float
from datetime import datetime

from database.config import Base


### TABLE project (input model (ProjectBase) and table columns (Project))
class ProjectBase(BaseModel):
    name: str
    description: str
    date_start: datetime
    date_predicted_conclusion: datetime
    date_conclusion: datetime
    developers_quantity: int
    develop_hours: int
    stack: str
    xp_level: str
    company_id: int
    company_field: str


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    description = Column(String(100), nullable=False)
    date_start = Column(DateTime, default=func.now(), nullable=False)
    date_predicted_conclusion = Column(DateTime, default=func.now(), nullable=False)
    date_conclusion = Column(DateTime, default=func.now())
    developers_quantity = Column(Integer)
    develop_hours = Column(Integer)
    stack = Column(String(100), nullable=False)
    xp_level = Column(String(100), nullable=False)
    company_id = Column(Integer, nullable=False)
    company_field = Column(String(100), nullable=False)
