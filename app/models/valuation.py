# models.py
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from database.config import Base


### TABLE valuation (input model (ValuationBase) and table columns (Valuation))
class ValuationBase(BaseModel):
    valuation: str
    user_id: int
    task_id: int

class Valuation(Base):
    __tablename__ = "valuations"

    id = Column(Integer, primary_key=True, index=True)
    valuation = Column(String(500), nullable=False)
    user_id = Column(Integer, nullable=True)
    task_id = Column(Integer, nullable=True)
