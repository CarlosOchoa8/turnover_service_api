-- migrate:up
CREATE TABLE "collaborator"
(
   id integer generated always as identity PRIMARY KEY,
   age integer not null,
   attrition varchar(255),
   business_travel varchar(255) not null,
   daily_rate integer not null,
   department varchar(255) not null,
   distance_from_home integer not null,
   education integer not null,
   education_field varchar(255) not null,
   employee_count integer not null,
   employee_number integer UNIQUE not null,
   environment_satisfaction integer not null,
   gender varchar(255) not null,
   hourly_rate integer not null,
   job_involvement integer not null,
   job_level integer not null,
   job_role varchar(255) not null,
   job_satisfaction integer not null,
   marital_status varchar(255) not null,
   monthly_income integer not null,
   monthly_rate integer not null,
   num_companies_worked integer not null,
   over_18 varchar(255) not null,
   over_time varchar(255) not null,
   percent_salary_hike integer not null,
   performance_rating integer not null,
   relationship_satisfaction integer not null,
   standard_hours integer not null,
   stock_option_level integer not null,
   total_working_years integer not null,
   training_times_last_year integer not null,
   work_life_balance integer not null,
   years_at_company integer not null,
   years_in_current_role integer not null,
   years_since_last_promotion integer not null,
   years_with_curr_manager integer not null
);

create unique index unique_employee_number on "collaborator" (employee_number);
-- migrate:down
DROP TABLE "collaborator"