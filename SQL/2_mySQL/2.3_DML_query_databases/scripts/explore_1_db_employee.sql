USE employees;

SELECT * FROM departments;
SELECT * FROM dept_emp;
SELECT * FROM dept_manager;
SELECT * FROM employees;
SELECT * FROM salaries;
SELECT * FROM titles;


# Indicar salarios atuais dos empregados

SELECT emp_no, salary  FROM salaries WHERE to_date > YEAR(CURRENT_DATE());