SELECT *
FROM parks_and_recreation.employee_salary
WHERE first_name = 'Leslie';

SELECT *
FROM parks_and_recreation.employee_salary
WHERE salary > 50000  ; -- selects the rows where salalry is greater than 50000

SELECT *
FROM parks_and_recreation.employee_demographics
WHERE gender = 'female';

SELECT *
FROM parks_and_recreation.employee_demographics
WHERE gender != 'female'; 

SELECT *
FROM parks_and_recreation.employee_demographics
WHERE birth_date > '1985-01-01'; -- anyone younger than this date

SELECT *
FROM parks_and_recreation.employee_demographics
WHERE birth_date > '1985-01-01'
AND gender = 'male' -- adds another condition
;

SELECT *
FROM parks_and_recreation.employee_demographics
WHERE birth_date > '1985-01-01'
OR gender = 'male' -- adds another condition
;

SELECT *
FROM parks_and_recreation.employee_demographics
WHERE birth_date > '1985-01-01'
OR NOT gender = 'male' -- adds another condition
;

SELECT *
FROM parks_and_recreation.employee_demographics
WHERE (first_name = 'Leslie' AND age = 44) OR age > 55

-----------------LIKE satement-----------------------
-- % doesnt matter how much characters to the left or right
-- _ onli=y fixed number of charcters
SELECT *
FROM parks_and_recreation.employee_demographics
WHERE first_name LIKE 'jer%'; -- doesnt matter how much characters to the left

SELECT *
FROM parks_and_recreation.employee_demographics
WHERE first_name LIKE '%er%'; -- it can be both at the front or at the bottom

SELECT *
FROM parks_and_recreation.employee_demographics
WHERE first_name LIKE 'jer__';

SELECT *
FROM parks_and_recreation.employee_demographics
WHERE first_name LIKE '_er__';

SELECT *
FROM parks_and_recreation.employee_demographics
WHERE birth_date LIKE '1989%';

