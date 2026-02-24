---GROUP BY is different from DISTINCT 
SELECT *
FROM parks_and_recreation.employee_demographics


SELECT gender, AVG(age)
FROM parks_and_recreation.employee_demographics
GROUP BY gender; -- gets the average of age of all the males and female

SELECT occupation, salary
FROM parks_and_recreation.employee_salary
GROUP BY occupation, salary

SELECT gender, AVG(age), MAX(age)
FROM parks_and_recreation.employee_demographics
GROUP BY gender; --  SELECTS the average age and maximum age of males and females

SELECT gender, AVG(age), MAX(age), MIN(age), COUNT(age)
FROM parks_and_recreation.employee_demographics
GROUP BY gender; --  SELECTS the average age and maximum age of males and females