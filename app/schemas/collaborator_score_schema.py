from pydantic import BaseModel, field_validator


class CollaboratorScoreBaseSchema(BaseModel):
    """
    A schema class representing the base attributes of a collaborator score.
    """
    employee_number: int
    score: float | str


class CollaboratorScoreCreateSchema(BaseModel):
    """
    A schema class representing the base attributes of a collaborator score.
    """
    employee_number: int
    score: float | str


class CollaboratorScoreResponseSchema(CollaboratorScoreBaseSchema):
    """
    A schema class representing response for collaborator score.
    """
    pass

    @field_validator("score")
    def convert_to_percentage(cls, value) -> str:
        """Convert to percetage for more readability."""
        return f"{round(value * 100, 2)}%"
