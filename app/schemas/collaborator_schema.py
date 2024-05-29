from typing import Any, ClassVar

from fastapi import HTTPException, status
from pydantic import (BaseModel, EmailStr, Field, field_validator,
                      model_validator, validator)


class CollaboratorBaseSchema(BaseModel):
    """
    A schema class representing the base attributes of a collaborator.
    """
    age: int
    attrition: str | None = None
    business_travel: str
    daily_rate: int
    department: str
    distance_from_home: int
    education: int
    education_field: str
    employee_count: int | None = None
    employee_number: int
    environment_satisfaction: int
    gender: str
    hourly_rate: int
    job_involvement: int
    job_level: int | None = None
    job_role: str
    job_satisfaction: int
    marital_status: str
    monthly_income: int
    monthly_rate: int
    num_companies_worked: int
    over_18: str | None = None
    over_time: str
    percent_salary_hike: int
    performance_rating: int
    relationship_satisfaction: int
    standard_hours: int | None = None
    stock_option_level: int
    total_working_years: int | None = None
    training_times_last_year: int
    work_life_balance: int
    years_at_company: int
    years_in_current_role: int
    years_since_last_promotion: int
    years_with_curr_manager: int

    # @field_validator('*')
    # def transform_keys(cls, v):
    #     if isinstance(v, dict):
    #         return {cls.transform_key(k): v for k, v in v.items()}
    #     return v

    # @classmethod
    # def transform_key(cls, key: str) -> str:
    #     return ''.join(['_' + i.lower() if i.isupper() else i for i in key]).lstrip('_')


class CollaboratorCreateSchema(CollaboratorBaseSchema):
    pass
