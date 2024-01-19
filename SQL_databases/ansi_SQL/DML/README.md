# Comandos de Consulta Avançados

## 1 - Cláusula SELECT

**Sintaxe**: SELECT [`value_1 | expression_1`, `value_2 | expression_2`, ...]

O statement SELECT recebe como parâmetro um valor ou expressão e os retorna. É possivel usar o SELECT com:

- Valores correspondentes aos tipos do SQL, tais como Strings ou Numeros e Booleanos;
- Valores associados a operadores algebricos [`+`, `-`, `*`, `/`];
- Valores associados a operadores lógicos [`AND`, `OR`, `NOT`, `>`, `<`, `>=`, `<=`, `<>`, `!=`];
- Valores associados a funções Built-in do MySQL;
- É possível selecionar mais de um valor podendo eles serem de diferentes tipos.

Exemplos:

- SELECT `'Hello World'`: Retorna a string 'Hello World'.
- SELECT `2 + 2`: Retorna o inteiro 4.
- SELECT `'Hello World'`, `2 + 2`: Retorna a string 'Hello World' e o inteiro 4.


## 2 - Operadores no SQL

Os operadores lógicos do SQL recebem esse nome porque sempre retornam `TRUE` ou `FALSE`.

### 2.1 - Operador NOT

**Sintaxe**: SELECT NOT `value`

- É aplicado a um valor booleano `value`;
- Retorna 1 se o valor `value` é 0;
- Retorna 0 se o valor `value` é 1;

Exemplos:

- SELECT NOT FALSE: retorna 1;
- SELECT NOT TRUE: retorna 0;

### 2.2 - Operador AND

**Sintaxe**: SELECT `value_1` AND `value_2`

- É aplicado a 2 valores booleanos `value_1` e `value_2`.
- Retorna 1 se `value_1` e `value_2` são 1.
- Retorna 0 se `value_1` ou `value_2` são 0. 

Exemplos:

- SELECT FALSE AND FALSE: retorna 0;
- SELECT TRUE AND FALSE: retorna 0;
- SELECT FALSE AND TRUE: retorna 0;
- SELECT TRUE AND TRUE: retorna 1;

### 2.3 - Operador OR

**Sintaxe**: SELECT `value_1` OR `value_2`

- É aplicado a 2 valores booleanos `value_1` e `value_2`.
- Retorna 1 se `value_1` ou `value_2` são 1.
- Retorna 0 se `value_1` e `value_2` são 0. 

Exemplos:

- SELECT FALSE OR FALSE: retorna 0;
- SELECT TRUE OR FALSE: retorna 1;
- SELECT FALSE OR TRUE: retorna 1;
- SELECT TRUE OR TRUE: retorna 1;

### 2.4 - Operadores lógicos de comparação

**Sintaxe**: SELECT `value_1` <operator> `value_2`

- É aplicado a 2 valores `value_1` e `value_2` que podem ser de qualquer tipo, desde que sejam iguais.
- Os operadores suportados pelo MySQL são [IS, =, >, < , >=, <=, <>, !=].
- O resultado de uma operação de comparação entre valores não booleanos sempre retornam 1 ou 0

Exemplos:

- SELECT 2 = 2: retorna 1;
- SELECT 2 != 1: retorna 1;


## 2.5 - Operador BETWEEN AND

**Sintaxe**: SELECT `value` BETWEEN `value_1` AND `value_n`

- Retorna 1 se o valor `value` está contido no intervalo (`value_1`, `value_n`);
- Retorna 0 se o valor `value` não está contido no intervalo (`value_1`, `value_n`);

OBS: O `value` pode ser uma string, inteiro, decimal, datetime. Cada um desses tipos possui ordenação entre seus valores.

Exemplos:

- SELECT 3 BETWEEN 1 AND 5: retorna 1;
- SELECT 7 BETWEEN 1 AND 5: retorna 0;
- SELECT 'B' BETWEEN 'A' AND 'C': retorna 1;
- SELECT 'D' BETWEEN 'A' AND 'C'; retorna 0;

## 2.6 - Operador IN

**Sintaxe**: SELECT `value` IN (`value_1`, `value_2`, ..., `value_n`)

- Retorna 1 se o valor `value` se encontra na lista (`value_1`, `value_2`, ..., `value_n`);
- Retorna 0 se o valor `value` se encontra na lista (`value_1`, `value_2`, ..., `value_n`);

## 2 - Selecionando dados de entidades do banco com o SELECT FROM


**Sintaxe**: SELECT [ `value_1 | col_1 | expression_1`, `value_2 | col_2 | expression_2`, ... ] FROM `table | view`

O statement SELECT aliado ao FROM torna possível selecionar colunas de uma tabela ou view do banco de dados.
Em um `SELECT FROM` puro sobre uma tabela é possível retornar:

- Retornar todas as colunas da tabela selecionada com o simbolo `*`.
- Retornar um subconjunto das colunas da tabela selecionada especificando o nome dessas colunas.
- Retornar novas colunas usando colunas existentes na tabela selecionada aliados a operadores do SQL.

Exemplos:

- **SELECT * FROM `database.tabela`**: Retorna todas as colunas da tabela.
- **SELECT `col_1`, `col_2`, ... FROM `database.tabela`**: Retorna somente as colunas da tabela especificadas após o SELECT.
- **SELECT `col_1`, `col_2`, `col_1 + col_2` FROM `database.tabela`**: Retorna as colunas col_1 e col_2 da tabela e cria coluna de soma entre ambas.

É importante notar que um SELECT FROM puro pode somente retornar o número de linhas total da tabela. Para que seja possível executar operações que retornem um subconjunto das linhas da tabela é usada a cláusula WHERE.



## 3 - Cláusula WHERE

- A cláusula **WHERE**, sempre usada na sequência da cláusula **SELECT FROM** 
- Tem por finalidade filtrar linhas que devem ser retornadas no **SELECT FROM**.
- A especificação das linhas a serem selecionadas se dá por meio de uma condição passada a cláusula **WHERE**.
- Caso a condição retorne TRUE a linha será selecionada. Caso contrário a linha não será selecionada.

**Sintaxe**: SELECT `*` FROM `table_name` WHERE `condition`


## LIKE

- Usado em filtros
- Caracteres especiais:
    - %: qualquer número de caracteres;
    - .: 


## 4 - DISTINCT


## 5 - LIMIT


## 6 - ORDER BY


## 7 - GROUP BY


## 8 - HAVING

O HAVING é uma condição ou filtro que se aplica ao resultado de uma agregação.

Após o GROUP BY

SELECT `col_a`, SUM(`col_b`) FROM `table_name` GROUP BY `col_a` HAVING SUM(`col_b`) >= `value`


## 9 - CASE

CASE
WHEN THEN
WHEN THEN
OTHERWISE


## 10 - Cláusulas do tipo JOIN

### 10.1 - INNER JOIN

**Sintaxe**: SELECT `a.col_1`, `b.col_1` FROM `tabela_esquerda` INNER JOIN `tabela_direita` ON `a.col_key` = `b.col_key`

### 10.2 - LEFT JOIN

**Sintaxe**: SELECT `a.col_1`, `b.col_1` FROM `tabela_esquerda` LEFT JOIN `tabela_direita` ON `a.col_key` = `b.col_key`

### 10.3 - RIGHT JOIN

**Sintaxe**: SELECT `a.col_1`, `b.col_1` FROM `tabela_esquerda` LEFT JOIN `tabela_direita` ON `a.col_key` = `b.col_key`


### 10.4 - CROSS JOIN

**Sintaxe**: SELECT `a.col_1`, `b.col_1` FROM `tabela_esquerda` LEFT JOIN `tabela_direita` ON `a.col_key` = `b.col_key`

### 10.5 - FULL JOIN


### 10.6 - UNION

Une 2 tabelas com numero de colunas, tipos e ordem??? verticalmente. Elimina linhas duplicadas naturalmente.
é equivalente de um DISTINCT * no resultado de um UNION ALL.

### 10.7 - UNION ALL

Une 2 tabelas com numero de colunas, tipos e ordem??? verticalmente. Não elimina linhas duplicadas.

## 11 - SUB QUERIES

3 tipos de subquery:

Subquery no WHERE

SUBQUERY NO FROM.


### 12 - VIEWs

Views são tabelas lógicas.

Por de baixo dos panos executam a query. 

CREATE VIEW `vw_view_name` AS SELECT * FROM `table_name`;
CREATE OR REPLACE VIEW `vw_view_name` AS SELECT * FROM `table_name`;