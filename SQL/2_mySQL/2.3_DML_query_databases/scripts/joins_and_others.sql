SELECT * FROM tabela_de_vendedores;
SELECT * FROM notas_fiscais;


SELECT * FROM tabela_de_vendedores a INNER JOIN notas_fiscais b ON a.MATRICULA = b.MATRICULA;


SELECT a.MATRICULA, a.NOME, COUNT(*) FROM tabela_de_vendedores a INNER JOIN notas_fiscais b ON a.MATRICULA = b.MATRICULA GROUP BY a.MATRICULA, a.NOME;
SELECT a.MATRICULA, a.NOME, COUNT(*) FROM tabela_de_vendedores a, notas_fiscais b WHERE a.MATRICULA = b.MATRICULA GROUP BY a.MATRICULA, a.NOME;

SELECT COUNT(*) FROM tabela_de_clientes;
SELECT CPF, COUNT(*) FROM notas_fiscais GROUP BY CPF;
SELECT DISTINCT a.CPF, a.NOME, b.CPF FROM tabela_de_clientes a INNER JOIN notas_fiscais b ON a.CPF = b.CPF;
SELECT DISTINCT a.CPF, a.NOME, b.CPF FROM tabela_de_clientes a LEFT JOIN notas_fiscais b ON a.CPF = b.CPF;
SELECT DISTINCT a.CPF, a.NOME, b.CPF FROM tabela_de_clientes a LEFT JOIN notas_fiscais b ON a.CPF = b.CPF WHERE b.CPF IS NULL;

SELECT * FROM tabela_de_vendedores;
SELECT * FROM tabela_de_clientes;
SELECT 
	tabela_de_vendedores.BAIRRO, 
	tabela_de_vendedores.NOME,
	tabela_de_clientes.BAIRRO,
    tabela_de_clientes.NOME
FROM tabela_de_vendedores INNER JOIN tabela_de_clientes ON tabela_de_vendedores.BAIRRO = tabela_de_clientes.BAIRRO;


SELECT BAIRRO FROM tabela_de_vendedores
UNION
SELECT BAIRRO FROM tabela_de_clientes;

SELECT BAIRRO FROM tabela_de_vendedores
UNION
SELECT BAIRRO FROM tabela_de_clientes;

SELECT DISTINCT * FROM
(SELECT BAIRRO FROM tabela_de_vendedores
UNION ALL
SELECT BAIRRO FROM tabela_de_clientes) a;

SELECT BAIRRO, NOME, 'VENDEDOR' AS TIPO_PESSOA FROM tabela_de_vendedores
UNION
SELECT BAIRRO, NOME, 'CLIENTE' AS TIPO_PESSOA FROM tabela_de_clientes;


SELECT DISTINCT BAIRRO FROM tabela_de_vendedores;
SELECT * FROM tabela_de_vendedores WHERE BAIRRO IN (SELECT DISTINCT BAIRRO FROM tabela_de_vendedores);

SELECT a.EMBALAGEM, a.PRECO_MAXIMO FROM
(SELECT EMBALAGEM, MAX(PRECO_DE_LISTA) AS PRECO_MAXIMO FROM tabela_de_produtos GROUP BY EMBALAGEM) a WHERE a.PRECO_MAXIMO > 10;


SELECT CPF, COUNT(*) AS COUNTER FROM notas_fiscais WHERE YEAR(DATA_VENDA) = 2016 GROUP BY CPF HAVING COUNT(*) > 2000;

SELECT * FROM
(SELECT CPF, COUNT(*) AS COUNTER FROM notas_fiscais WHERE YEAR(DATA_VENDA) = 2016 GROUP BY CPF) a WHERE COUNTER > 2000;
