from typing import Any, ClassVar

from fastapi import HTTPException, status
from pydantic import (BaseModel, EmailStr, Field, field_validator,
                      model_validator)


class CollaboratorBaseSchema(BaseModel):
    """
    A schema class representing the base attributes of a collaborator.
    """
    age: int
    attrition: str
    business_travel: str
    daily_rate: int
    department: str
    distance_from_home: int
    education: int
    education_field: str
    employee_number: int
    environment_satisfaction: int
    gender: str
    hourly_rate: int
    job_involvement: int
    job_role: str
    job_satisfaction: int
    marital_status: str
    monthly_income: int
    monthly_rate: int
    num_companies_worked: int
    over_time: str
    percent_salary_hike: int
    performance_rating: int
    relationship_satisfaction: int
    stock_option_level: int
    training_times_last_year: int
    work_life_balance: int
    years_at_company: int
    years_in_current_role: int
    years_since_last_promotion: int
    years_with_curr_manager: int

class CollaboratorCreateSchema(CollaboratorBaseSchema):
    pass

class CollaboratorUpdateSchema(BaseModel):
    pass
