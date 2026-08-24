CREATE SCHEMA IF NOT EXISTS lab;

CREATE TABLE IF NOT EXISTS lab.customers (
    customer_id  INTEGER PRIMARY KEY,
    first_name   TEXT NOT NULL,
    last_name    TEXT NOT NULL,
    email        TEXT,
    city         TEXT,
    signup_date  DATE,
    customer_segment  TEXT,
    CONSTRAINT ck_customer_id_positive CHECK (customer_id > 0)
);