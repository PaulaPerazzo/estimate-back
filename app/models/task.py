# models.py
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, func
from sqlalchemy.orm import relationship
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
    develop_predict_hours: float
    problems: str
    keywords: str
    requirements: str
    framework: str
    libs: str
    sugestions: str
    task_action: str
    component_action: str
    seniority: str
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
    develop_predict_hours = Column(Float)
    problems = Column(String(200))
    keywords = Column(String(100), nullable=True)
    requirements = Column(String(300))
    framework = Column(String(100))
    libs = Column(String(300))
    sugestions = Column(String(300))
    task_action = Column(String(300))
    component_action = Column(String(300))
    seniority = Column(String(300))

    user_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"))
    user = relationship("User", back_populates="tasks")

    project_id = Column(Integer, ForeignKey("projects.id", ondelete="SET NULL"), nullable=True)
    project = relationship("Project", back_populates="tasks")

    valuations = relationship("Valuation", back_populates="task")
