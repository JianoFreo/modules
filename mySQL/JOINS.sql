SELECT *
FROM parks_and_recreation.employee_demographics;

SELECT dem.employee_id, age 
FROM parks_and_recreation.employee_demographics AS dem
INNER JOIN parks_and_recreation.employee_salary AS sal
    ON dem.employee_id = sal.employee_id;