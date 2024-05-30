from sqlalchemy.orm import Session, joinedload

from app.crud.base_crud import CRUDBuilder
from app.models import Collaborator as CollaboratorModel


class CRUDCollaborator(CRUDBuilder):
    """
    CRUD class object with default methods to Create and Read for CollaboratorModel
    """
    def get_collaborator_by_id(self, collaborator_id: int, db: Session) -> CollaboratorModel:
        return db.query(self.model).options(
            joinedload(self.model.collaborator_score)
            ).filter(self.model.employee_number == collaborator_id).first()

crud_collaborator = CRUDCollaborator(CollaboratorModel)
