SELECT LTRIM('           OIIIII') AS TRIM_FUNCT UNION ALL
SELECT RTRIM('OIIIII           ') UNION ALL
SELECT TRIM('    OIIIII        ');

SELECT CONCAT('Dadaia', ' ', 'Data Engineer') AS CUMPRIMENTO  UNION ALL
SELECT LOWER('Dadaia Data Engineer')  UNION ALL
SELECT UPPER('Dadaia Data Engineer');


SELECT SUBSTRING('Dadaia Data Engineer', 1, 6);
SELECT SUBSTRING('Dadaia Data Engineer', 7, 14);


