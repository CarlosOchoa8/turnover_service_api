"""
Generate an Object of CRUD
"""
from typing import Any

import numpy as np
from sqlalchemy import insert
from sqlalchemy.orm import Session
from app.crud.base_crud import CRUDBuilder
from app.models import CollaboratorScore as CollaboratorScoreModel
from app.schemas import CollaboratorCreateSchema


class CRUDCollaboratorScore(CRUDBuilder):
    """Item CRUD class

    Args:
        CRUDBase ([Item, ItemCreate, ItemUpdate])
    """
    def __init__(self, model) -> None:
        self.model = model

    def create(self, db: Session, obj_in: CollaboratorCreateSchema | dict[str | Any]) -> CollaboratorScoreModel:
        """Create a collaborator score object"""
        obj_in_data = obj_in if isinstance(obj_in, dict) else obj_in.dict()
        for field, value in obj_in_data.items():
            if np.issubdtype(value, np.int64):
                obj_in_data.update({field: int(value)})
            if np.issubdtype(value, np.float64):
                obj_in_data.update({field: float(value)})
        db_obj = self.model(**obj_in_data)  # type: ignore
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_collaborator_id(self, collaborator_id: int, db: Session) -> CollaboratorScoreModel:
        return db.query(self.model).filter(self.model.employee_number == collaborator_id).first()


crud_collaborator_score = CRUDCollaboratorScore(CollaboratorScoreModel)
