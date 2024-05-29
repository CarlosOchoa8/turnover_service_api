from sqlalchemy import Column, Integer, String

from app.database.base_class import Base


class Collaborator(Base):
    __tablename__  = "collaborator"

    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer, nullable=False)
    attrition = Column(String, nullable=True)
    business_travel = Column(String, nullable=False)
    daily_rate = Column(Integer, nullable=False)
    department = Column(String, nullable=False)
    distance_from_home = Column(Integer, nullable=False)
    education = Column(Integer, nullable=False)
    education_field = Column(String, nullable=False)
    employee_count = Column(Integer, nullable=False)
    employee_number = Column(Integer, nullable=False, unique=True)
    environment_satisfaction = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)
    hourly_rate = Column(Integer, nullable=False)
    job_involvement = Column(Integer, nullable=False)
    job_level = Column(Integer, nullable=False)
    job_role = Column(String, nullable=False)
    job_satisfaction = Column(Integer, nullable=False)
    marital_status = Column(String, nullable=False)
    monthly_income = Column(Integer, nullable=False)
    monthly_rate = Column(Integer, nullable=False)
    num_companies_worked = Column(Integer, nullable=False)
    over_18 = Column(String, nullable=False)
    over_time = Column(String, nullable=False)
    percent_salary_hike = Column(Integer, nullable=False)
    performance_rating = Column(Integer, nullable=False)
    relationship_satisfaction = Column(Integer, nullable=False)
    standard_hours = Column(Integer, nullable=False)
    stock_option_level = Column(Integer, nullable=False)
    total_working_years = Column(Integer, nullable=False)
    training_times_last_year = Column(Integer, nullable=False)
    work_life_balance = Column(Integer, nullable=False)
    years_at_company = Column(Integer, nullable=False)
    years_in_current_role = Column(Integer, nullable=False)
    years_since_last_promotion = Column(Integer, nullable=False)
    years_with_curr_manager = Column(Integer, nullable=False)
