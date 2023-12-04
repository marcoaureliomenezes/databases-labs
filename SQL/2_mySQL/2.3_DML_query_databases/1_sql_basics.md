## 1 - Cláusula SELECT

- A cláusula **SELECT** é usada para retornar um valor.
- Recebe como parametro 1 ou mais valores ou expressões, separados por vírgula.

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