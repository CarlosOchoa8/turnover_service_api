from app.schemas import CollaboratorCreateSchema

collaborator_data =  {
                "age": 30,
                "attrition": "No",
                "business_travel": "Travel_Rarely",
                "daily_rate": 750,
                "department": "Sales",
                "distance_from_home": 10,
                "education": 4,
                "education_field": "Marketing",
                "employee_count": 1,
                "employee_number": 12345,
                "environment_satisfaction": 3,
                "gender": "Male",
                "hourly_rate": 35,
                "job_involvement": 3,
                "job_level": 2,
                "job_role": "Sales Executive",
                "job_satisfaction": 4,
                "marital_status": "Married",
                "monthly_income": 6000,
                "monthly_rate": 12000,
                "num_companies_worked": 2,
                "over_18": "Y",
                "over_time": "Yes",
                "percent_salary_hike": 15,
                "performance_rating": 3,
                "relationship_satisfaction": 2,
                "standard_hours": 8,
                "stock_option_level": 1,
                "total_working_years": 10,
                "training_times_last_year": 2,
                "work_life_balance": 3,
                "years_at_company": 5,
                "years_in_current_role": 3,
                "years_since_last_promotion": 1,
                "years_with_curr_manager": 2
}

collaborator_in = CollaboratorCreateSchema(**collaborator_data)
collaborator_id = collaborator_data.get("employee_number")
collaborator_id_fake = 99999
