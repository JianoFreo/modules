SELECT *
FROM parks_and_recreation.employee_demographics;

SELECT first_name, last_name, birth_date
FROM parks_and_recreation.employee_demographics;

SELECT first_name,
last_name, 
birth_date,
age,
age + 10 -- adds 10 to the age
FROM parks_and_recreation.employee_demographics;

SELECT first_name,
last_name, 
birth_date,
age,
(age + 10) * 10 -- pemdas
FROM parks_and_recreation.employee_demographics;

SELECT DISTINCT gender -- only grabs the distinct values/ doesnt duplicate
FROM parks_and_recreation.employee_demographics;

SELECT DISTINCT first_name, gender -- still prints the duplicates of gender beacsue the names are all unique
FROM parks_and_recreation.employee_demographics;