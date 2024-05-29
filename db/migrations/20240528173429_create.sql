-- migrate:up
CREATE TABLE "collaborator_score"
(
   id integer generated always as identity PRIMARY KEY,
   employee_number integer not null,
   score double precision not null,

   constraint fk_employee_number foreign key (employee_number) references "collaborator"(employee_number) on delete cascade
);

-- migrate:down
DROP TABLE "collaborator_score"