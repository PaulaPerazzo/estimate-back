# models.py
from pydantic import BaseModel
from sqlalchemy import Column, ForeignKey, Integer, String
from database.config import Base
from sqlalchemy.orm import relationship

### TABLE valuation (input model (ValuationBase) and table columns (Valuation))
class ValuationBase(BaseModel):
    valuation: str
    user_id: int
    task_id: int

class Valuation(Base):
    __tablename__ = "valuations"

    id = Column(Integer, primary_key=True, index=True)
    valuation = Column(String(500), nullable=False)

    user_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"))
    user = relationship("User", back_populates="valuations")

    task_id = Column(Integer, ForeignKey("tasks.id", ondelete="SET NULL"))
    task = relationship("Task", back_populates="valuations")
