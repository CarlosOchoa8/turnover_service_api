"""
Generate an Object of CRUD
"""
from sqlalchemy.orm import Session
from app.config.database.crud_base import CRUDBase
from app.models import Collaborator as CollaboratorModel
from app.schemas import CollaboratorCreateSchema, CollaboratorUpdateSchema


class CRUDCollaborator(CRUDBase[CollaboratorModel, CollaboratorCreateSchema, CollaboratorUpdateSchema]):
    """Item CRUD class

    Args:
        CRUDBase ([Item, ItemCreate, ItemUpdate])
    """


crud_collaborator = CRUDCollaborator(CollaboratorModel)
