# Stored Procedures


- Linguagem estruturada para bancos de dados SQL.

- Não segue um padrão ANSI.
- Comandos de repetição e 


Requisitos para nomes de Stored Procedures:

- Nome deve ter apenas letras, numeros, `$` e `_`;
- tamanho máximo 64 caracteres;
- case sensitive;
- Nome deve ser único;


CREATE PROCEDURE
procedure_name(parameters)
BEGIN

VARCHAR(n)
INTEGER
DECIMAL(p, s)
DATE
DECLARE declaration_statement
...
executable_code
...



Declaração de variável:

Exemplos:

DECLARE `var_1` VARCHAR(6) DEFAULT 'valor_1'
DECLARE `var_1`, `var_2` VARCHAR(6) DEFAULT 'valor_1'


SET `var_1` = 'novo_valor'
### Command to exeute stored procedure

CALL `procedure_name()`

