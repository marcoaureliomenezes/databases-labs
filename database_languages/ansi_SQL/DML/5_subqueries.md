# SUBQUERIES


USE employees;
SELECT * FROM titles;
SELECT * FROM dept_manager;
SELECT * FROM departments;
SELECT * FROM employees;


SELECT * FROM employees_dup;


SELECT *
	FROM dept_manager
    WHERE emp_no IN (SELECT emp_no FROM employees WHERE hire_date BETWEEN '1990-01-01' AND '1995-01-01');
    
    
SELECT 
	e.first_name, e.last_name
    FROM
		employees e
	WHERE
    EXISTS(SELECT * FROM dept_manager dm WHERE dm.emp_no = e.emp_no);
    
SELECT 
	*
    FROM
		employees e
	WHERE
    EXISTS(SELECT * FROM titles t WHERE t.emp_no = e.emp_no AND t.title = 'Assistant Engineer');
    
INSERT INTO emp_manager SELECT U.* FROM 
	 (SELECT A.*
	 FROM
		(SELECT
			e.emp_no AS employee_ID,
			MIN(de.dept_no) AS department_code,
			(SELECT
					emp_no
				FROM dept_manager
				WHERE emp_no = 110022
			) AS manager_id
		FROM employees e
		JOIN dept_emp de ON e.emp_no = de.emp_no
		WHERE e.emp_no <= 10020
		GROUP BY e.emp_no
		ORDER BY e.emp_no) A
	UNION SELECT
		B.* 
	FROM
		(SELECT
			e.emp_no AS employee_ID,
			MIN(de.dept_no) AS department_code,
			(SELECT
					emp_no
				FROM dept_manager
				WHERE emp_no = 110039
			) AS manager_id
		FROM employees e
		JOIN dept_emp de ON e.emp_no = de.emp_no
		WHERE e.emp_no BETWEEN 10021 AND 10040
		GROUP BY e.emp_no
		ORDER BY e.emp_no) B
	UNION SELECT C.*
	FROM
		(SELECT 
			e.emp_no AS employee_ID,
			MIN(de.dept_no) AS department_code,
			(SELECT
					emp_no
				FROM dept_manager
				WHERE emp_no = 110039
			) AS manager_id
			FROM employees e
			JOIN dept_emp de ON e.emp_no = de.emp_no
			WHERE e.emp_no = 110022
			GROUP BY e.emp_no
			ORDER BY e.emp_no) C
	UNION SELECT D.*
	FROM
		(SELECT 
			e.emp_no AS employee_ID,
			MIN(de.dept_no) AS department_code,
			(SELECT
					emp_no
				FROM dept_manager
				WHERE emp_no = 110022
			) AS manager_id
			FROM employees e
			JOIN dept_emp de ON e.emp_no = de.emp_no
			WHERE e.emp_no = 110039
			GROUP BY e.emp_no
			ORDER BY e.emp_no) D
		) U;