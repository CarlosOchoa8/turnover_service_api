from typing import Any

from fastapi.encoders import jsonable_encoder
from sqlalchemy import insert
from sqlalchemy.orm import Session, joinedload
from app.crud.base_crud import CRUDBuilder
from app.models import Collaborator as CollaboratorModel
from app.models import CollaboratorScore as CollaboratorScoreModel
from app.schemas import CollaboratorCreateSchema


class CRUDCollaborator(CRUDBuilder):


    def __init__(self, model) -> None:
        self.model = model

    def create(self, db: Session, obj_in: CollaboratorCreateSchema | dict[str, Any]) -> CollaboratorModel:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_collaborator_by_id(self, collaborator_id: int, db: Session) -> CollaboratorModel:
        return db.query(self.model).options(
            joinedload(self.model.collaborator_score)
            ).filter(self.model.employee_number == collaborator_id).first()

crud_collaborator = CRUDCollaborator(CollaboratorModel)
