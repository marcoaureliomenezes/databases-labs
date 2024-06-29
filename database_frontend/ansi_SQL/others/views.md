
    
CREATE OR REPLACE VIEW v_dept_emp_latest_date AS
SELECT
	emp_no, 
    MAX(from_date) AS from_date, 
    MAX(to_date) AS to_date
FROM dept_emp 
GROUP BY emp_no;

CREATE OR REPLACE VIEW v_average_dept_manager_salary AS
SELECT AVG(s.salary)
FROM
	dept_manager dm
    JOIN salaries s
    ON dm.emp_no = s.emp_no
