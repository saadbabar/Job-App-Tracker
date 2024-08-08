CREATE TABLE companies (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE positions (
    id SERIAL PRIMARY KEY,
    company_id INT REFERENCES companies(id),
    position_name VARCHAR(255) NOT NULL,
    application_date DATE NOT NULL,
    assessment_due_date DATE
);


ALTER TABLE positions ADD CONSTRAINT unique_position_per_company UNIQUE (company_id, position_name);
