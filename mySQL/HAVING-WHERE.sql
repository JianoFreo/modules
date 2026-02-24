SELECT gender, AVG(age)
FROM employee_demographics
GROUP BY gender
HAVING AVG(age) > 40;


SELECT occupation, AVG(salary)
FROM employee_salary
WHERE occupation LIKE '%manager'
GROUP BY occupation
HAVING AVG(salary) > 75000;

-- WHERE occupation LIKE '%manager' - First filters to only include rows where the occupation ends with "manager" (like "Sales Manager", "Project Manager", etc.)
-- GROUP BY occupation - Groups those filtered rows by occupation type
-- SELECT occupation, AVG(salary) - For each group, shows the occupation name and calculates the average salary
-- HAVING AVG(salary) > 75000 - Only shows occupation groups where the average salary exceeds $75,000


SELECT *
FROM parks_and_recreation.employee_demographics
ORDER BY age DESC
LIMIT 3; --limits the number of rows

SELECT *
FROM parks_and_recreation.employee_demographics
ORDER BY age DESC
LIMIT 2, 1;

-----ALIASING

SELECT gender, AVG(age) AS avg_age
FROM parks_and_recreation.employee_demographics
GROUP BY gender
HAVING AVG(age) > 40;








