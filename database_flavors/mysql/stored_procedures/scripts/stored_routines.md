USE employees;
DELIMITER $$

CREATE PROCEDURE select_employees()
BEGIN
	SELECT * FROM employees
    LIMIT 1000;
END$$

CREATE PROCEDURE average_salary()
BEGIN
	SELECT AVG(salary) FROM salaries
    LIMIT 1000;
END$$

DELIMITER ;

USE employees;
DELIMITER $$
CREATE PROCEDURE emp_avg_salary(IN p_emp_no INTEGER)
BEGIN
	SELECT 
		MAX(e.first_name), MAX(e.last_name), AVG(s.salary)
	FROM employees e
    JOIN salaries s
    ON e.emp_no = s.emp_no
    WHERE e.emp_no = p_emp_no
    LIMIT 1000;
END$$

CREATE PROCEDURE emp_avg_salary_out(IN p_emp_no INTEGER, OUT p_avg_salary DECIMAL(10, 2))
BEGIN
	SELECT 
		AVG(s.salary) INTO p_avg_salary
	FROM employees e
    JOIN salaries s
    ON e.emp_no = s.emp_no
    WHERE e.emp_no = p_emp_no;
END$$

CREATE PROCEDURE emp_info(IN first_name VARCHAR(256), IN last_name VARCHAR(256), OUT emp_no DECIMAL(10, 2))
BEGIN
	SELECT 
		emp_no INTO emp_no
	FROM employees e
    WHERE e.first_name = first_name AND e.last_name = last_name;
END$$

DELIMITER ;


CALL select_employees();
CALL average_salary();

CALL select_salaries(11300);
CALL emp_avg_salary(11300);

SET @v_avg_salary = 0;
CALL emp_avg_salary_out(11300, @v_avg_salary);
SELECT @v_avg_salary;

SET @v_emp_no = 0;
CALL emp_info('Aruna', 'Journel', @v_emp_no);
SELECT @v_emp_no;



# USER DEFINED FUNCTIONS

CREATE FUNCTION f_emp_avg_salary(p_emp_no INTEGER) RETURNS DECIMAL(10, 2)
DETERMINISTIC
BEGIN
	DECLARE v_avg_salary DECIMAL(10,2);
	SELECT
		AVG(s.salary) INTO v_avg_salary
		FROM employees e
		JOIN salaries s
		ON e.emp_no = s.emp_no
		WHERE e.emp_no = p_emp_no;
	RETURN v_avg_salary;
END$$

SELECT f_emp_Avg_salary(11300);


DELIMITER $$

CREATE FUNCTION f_emp_info(p_first_name VARCHAR(256), p_last_name VARCHAR(256)) RETURNS INTEGER
DETERMINISTIC
BEGIN
	DECLARE v_max_from_date DATE;
    DECLARE v_salary DECIMAL(10,2);
    SELECT 
		MAX(from_date) INTO v_max_from_date
		FROM employees e
        JOIN salaries s ON e.emp_no = s.emp_no
		WHERE e.first_name = p_first_name AND e.last_name = p_last_name;
        
	SELECT
		s.salary INTO v_salary
		FROM employees e
        JOIN salaries s ON e.emp_no = s.emp_no
		WHERE e.first_name = p_first_name AND e.last_name = p_last_name AND s.from_date = v_max_from_date;
	RETURN v_salary;
END$$

DELIMITER ;

SELECT f_emp_info('Aruna', 'Journel')