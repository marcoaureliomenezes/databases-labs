# JOINS e UNIONS


![Figura 3: Exemplo de um registro imutável](./img/schema.png)



###  RETORNAR FUNCIONÁRIOS QUE FORAM CHEFES DE DEPARTAMENTO (ID, FIRST_NAME E LAST NAME). MOSTRAR TAMBEM PERIODO NO CARGO
SELECT e.emp_no, 
		e.first_name, 
        e.last_name, 
        dm.dept_no, 
        dm.from_date, 
        dm.to_date,
       ROUND((UNIX_TIMESTAMP(dm.to_date) - UNIX_TIMESTAMP(dm.from_date)) / (60 * 60 * 24))
	FROM dept_manager dm INNER JOIN employees e 
    ON e.emp_no = dm.emp_no
    ORDER BY dm.from_date;



# INNER JOINS OLD AND NEW SYNTAX

SELECT e.emp_no, e.first_name, e.last_name, dm.dept_no, e.hire_date
FROM employees e, dept_manager dm
WHERE e.emp_no = dm.emp_no;

SELECT e.emp_no, e.first_name, e.last_name, dm.dept_no, e.hire_date
FROM employees e
INNER JOIN dept_manager dm
ON e.emp_no = dm.emp_no;


# LEFT JOINS


USE employees;
SELECT * FROM dept_manager_dup;
SELECT * FROM departments_dup ORDER BY dept_no;

SELECT
	m.dept_no, m.emp_no, d.dept_name
FROM dept_manager_dup m
LEFT JOIN departments_dup d
ON m.dept_no = d.dept_no
ORDER BY m.dept_no;

SELECT
	d.dept_no, m.emp_no, d.dept_name
FROM departments_dup d 
LEFT JOIN dept_manager_dup m
ON m.dept_no = d.dept_no
ORDER BY d.dept_no;


### Exercício

SELECT e.emp_no, e.first_name, e.last_name, dm.dept_no, dm.from_date

FROM employees e
LEFT JOIN dept_manager dm
ON e.emp_no = dm.emp_no
WHERE e.last_name = 'Markovitch'
ORDER BY dept_no DESC, emp_no;



# CROSS JOINS

SELECT dm.*, d.*, e.*
	FROM dept_manager dm
    CROSS JOIN departments d
    JOIN employees e 
    ON dm.emp_no = e.emp_no
    WHERE d.dept_no <> dm.dept_no
    ORDER BY dm.emp_no, d.dept_no
    ;
    
SELECT dm.*, d.*
	FROM dept_manager dm,  departments d
    ORDER BY dm.emp_no, d.dept_no;
    
SELECT dm.*, d.*
	FROM dept_manager dm
    JOIN departments d
    ORDER BY dm.emp_no, d.dept_no;
    
# MULTIPLE JOINS 

SELECT
	FIRST(e.emp_no), e.gender, AVG(s.salary) AS average_salary
FROM employees e
JOIN salaries s
ON e.emp_no = s.emp_no
GROUP BY e.gender;


SELECT
	e.first_name,
    e.last_name,
    e.hire_date,
    dm.from_date,
    d.dept_name
    FROM employees e
    JOIN dept_manager dm ON e.emp_no = dm.emp_no
    JOIN departments d ON dm.dept_no = d.dept_no;
    
    
SELECT
	e.first_name,
    e.last_name,
    e.hire_date,
    t.title,
    dm.from_date,
    d.dept_name
FROM employees e
JOIN dept_manager dm ON e.emp_no = dm.emp_no
JOIN departments d ON dm.dept_no = d.dept_no
JOIN titles t ON e.emp_no = t.emp_no
WHERE t.title = 'Manager'
ORDER BY e.emp_no;