SELECT *
FROM parks_and_recreation.employee_demographics
ORDER BY first_name ASC;

SELECT *
FROM parks_and_recreation.employee_demographics
ORDER BY first_name DESC;

SELECT *
FROM parks_and_recreation.employee_demographics
ORDER BY gender, age; -- the gender gets ordered first/gende is the first priority to get ordered

SELECT *
FROM parks_and_recreation.employee_demographics
ORDER BY 5, 4