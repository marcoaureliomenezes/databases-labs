USE employees;

SELECT COUNT(salary) FROM employees.salaries;
SELECT COUNT(DISTINCT(from_date)) FROM salaries;
SELECT COUNT(DISTINCT(dept_no)) FROM dept_emp;

SELECT SUM(salary) FROM salaries;
SELECT SUM(salary) FROM salaries WHERE from_date > '1997-01-01';

SELECT MIN(salary) FROM salaries;
SELECT MAX(salary) FROM salaries;

SELECT AVG(salary) FROM salaries;
SELECT AVG(salary) FROM salaries WHERE from_date > '1997-01-01';

SELECT ROUND(AVG(salary)) AS avg_salary , ROUND(AVG(salary), 2) AS avg_salary_rounded
	FROM salaries WHERE from_date > '1997-01-01';

SELECT * FROM departments_dup;

SELECT dept_no, dept_name, IFNULL(dept_name, 'Any department name') AS department_name
	FROM departments_dup;
    
SELECT COALESCE(dept_name, dept_manager, 'DEFAULT VALUE') AS 'coalesce' FROM departments_dup;

SELECT * FROM departments_dup;

SELECT dept_no, dept_name, COALESCE(dept_name, dept_no) AS 'dept_info', IFNULL(dept_name, 'N/A') 
	FROM departments_dup ORDER BY dept_no ASC;
    