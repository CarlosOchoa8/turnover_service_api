import re
from typing import Tuple

import joblib
import pandas as pd
from fastapi import APIRouter, Depends, HTTPException, UploadFile, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.crud import crud_collaborator, crud_collaborator_score
from app.database.db import get_db
from app.schemas import (CollaboratorCreateSchema,
                         CollaboratorScoreResponseSchema)
from app.utils.collaborator_processor import (multiple_collaborators,
                                              single_collaborator)

router = APIRouter()

@router.get("/score/{collaborator_id}", status_code=200)
def get_collaborator_score(collaborator_id: int, db: Session = Depends(get_db)):
    """ Return corresponding score for a collaborator by id."""

    if collaborator_score := crud_collaborator_score.get_by_collaborator_id(collaborator_id=collaborator_id, db=db):
        return collaborator_score
    raise HTTPException(
        detail=f"Collaborator {collaborator_id} does not have record.",
        status_code=status.HTTP_404_NOT_FOUND
    )


@router.post("/", response_model= CollaboratorScoreResponseSchema, status_code=200)
def create(collaborator_in: CollaboratorCreateSchema,
           db: Session = Depends(get_db)) -> JSONResponse | CollaboratorScoreResponseSchema:
    """Store new collaborator and generates a score for him.""" 
    collaborator_id = collaborator_in.employee_number
    if collaborator := crud_collaborator.get_collaborator_by_id(
        collaborator_id=collaborator_id,db=db
        ):
        collab_number = collaborator.collaborator_score[0].employee_number
        collab_score = collaborator.collaborator_score[0].score
        return JSONResponse(
            content={"message": f"Collaborator {collaborator_id} is already registered.",
                     "collaborator id": collab_number,
                     "collaborator score": collab_score},
                     status_code=200
                     )
    try:
        dict_to_predict = collaborator_in.model_dump()

        fields = [
            'employee_count',
            'attrition',
            'job_level',
            'over18',
            'standard_hours',
            'total_working_years'
            ]
        for key in fields:
            dict_to_predict.pop(key, None)

        data_frame = pd.DataFrame([dict_to_predict])
        data_frame.columns = single_collaborator.update_columns(data_frame)
        obj_in = single_collaborator.process_data(data_frame)

        crud_collaborator.create(obj_in=collaborator_in, db=db)
        return crud_collaborator_score.create(db=db, obj_in=obj_in)
    except Exception as exc:
        raise HTTPException(
            detail=f"Error adding collaborator.{str(exc)}",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        ) from exc

@router.post("/add_collaborators", status_code=200)
def upload_csv(file: UploadFile, db: Session = Depends(get_db)) -> JSONResponse:
    """ 
    Processes a CSV file coantaining collaborator data,
    creates collaborators and their score and adds them to the database.
    """
    # clf_model = joblib.load("clf.zahoree")
    collaborators_csv = pd.read_csv(file.filename)

    collaborators_copy = collaborators_csv.copy()
    collaborators_copy.columns = multiple_collaborators.update_columns(collaborators_csv)
    collaborators_list = [
    CollaboratorCreateSchema(**row.to_dict()) for _, row in collaborators_copy.iterrows()
    ]

    collaborators_score_list = multiple_collaborators.process_data(collaborators_csv)

    crud_collaborator.create_bulk(db=db, obj_in=collaborators_list)
    crud_collaborator_score.create_bulk(db=db, obj_in=collaborators_score_list)

    return JSONResponse(
        content={"message": "The collaborators and their scores were added correctly."}
    )




collaborator_router = router
