from sqlalchemy import Column, Integer
from database.config import Base


### TABLE user_project (table columns (UserProject))
class UserProject(Base):
    __tablename__ = "user_projects"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    project_id = Column(Integer, nullable=False)
 