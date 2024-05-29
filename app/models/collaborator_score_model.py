from sqlalchemy import Column, Float, ForeignKey, Integer
from sqlalchemy.orm import Relationship

from app.database.base_class import Base


class CollaboratorScore(Base):
    __tablename__  = "collaborator_score"
    id = Column(Integer, primary_key=True, index=True)
    employee_number = Column(Integer, ForeignKey("collaborator.employee_number"))
    score = Column(Float, nullable=False)
