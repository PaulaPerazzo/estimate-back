# models.py
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, DateTime, func, Float
from datetime import datetime
from database.config import Base


### TABLE task (input model (TaskBase) and table columns (Task))
class TaskBase(BaseModel):
    name: str
    description: str
    date_start: datetime
    date_predicted_conclusion: datetime
    date_conclusion: datetime
    develop_hours: float
    problems: str
    keywords: str
    requirements: str
    framework: str
    libs: str
    sugestions: str
    action: str
    user_id: int
    project_id: int


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    description = Column(String(100), nullable=False)
    date_start = Column(DateTime, default=func.now(), nullable=False)
    date_predicted_conclusion = Column(DateTime, nullable=False)
    date_conclusion = Column(DateTime, default=func.now())
    develop_hours = Column(Float)
    problems = Column(String(200))
    keywords = Column(String(100), nullable=True)
    requirements = Column(String(300))
    framework = Column(String(100))
    libs = Column(String(300))
    sugestions = Column(String(300))
    action= Column(String(300))
    user_id = Column(Integer, nullable=True)
    project_id = Column(Integer, nullable=True)
