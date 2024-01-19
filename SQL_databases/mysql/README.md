# MySQL Reviews


### MySQL Data Types


- View: Tabela lógica
- Stored Procedures: Diferentes entre cada SGBD (Postgre, Mysql, SQL Server, etc)
- Funções: Built-ins e customizadas.
- Triggers: Quando acontecer algo, faça isso.

## 3 - Tipos de dados


### 3.1 - Campos do tipos numéricos


### 3.1.1 - Tipos Inteiros:

Armazena numeros em bytes. Cada byte tem 8 bits, podendo ter 2**8 valores diferentes.

    TINYINT     1 Bytes 255
    SMALLINT    2 Bytes 65535
    MEDIUMINT   3 Bytes 16777215
    INT         4 Bytes 4294967295
    BIGINT      8 Bytes 2**64 - 1

Propriedades:

- **SIGNED**: Contabiliza números negativos e positivos.
- **UNSIGNED**: Contabiliza somente números positivos.
- **AUTO_INCREMENT**: Sequência auto incrementada.
- **Erros do tipo OUT OF RANGE**: Quando se tenta gravar no banco de dados um valor fora do permitido pela definição do tipo do dado.
- **ZEROFILL**: Preenche com Zeros os espaços:
    Exemplo: INT(4) Se armazenarmos o valor 5 será gravado 0005


### 3.1.2 - Tipos Pontos Flutuantes

Diferença entre FLOAT e DOUBLE: Tamanho de armazenamento. Float é precisão simples e Double é precisão dupla.

FLOAT(`num_digits`, `decimal_size`)

    FLOAT       4 Bytes
    DOUBLE      8 Bytes

### 3.1.3 - Tipo decimal fixos

Número desse tipo pode ter até 65 dígitos.

- DECIMAL(`num_digits`, `decimal_size`)
- NUMERIC(`num_digits`, `decimal_size`)

Exemplos:

- DECIMAL(5,2) = {-999.99, 999.99}
- DECIMAL(7,2) = {-999.9999, 999.9999}
- DECIMAL(7,4) = {-999.9999, 999.9999}

### 3.1.4 - Tipo Binários

Usado para armazenar bits.

- BIT(`num_bits`)

Exemplos:

- BIT(1) = 0 | 1
- BIT(2) = 00 | 01 | 10 | 11


### 3.2 - Campos do tipos Data e Hora

- DATE: Format={`YYYY-MM-DD`}, LIMITS={`1000-01-01` to `9999-12-31`}
- DATETIME: Format={`YYYY-MM-DD HH:MM:SS`}  LIMITS={`1000-01-01 00:00:00` to `9999-12-31 23:59:59`}
- TIMESTAMP: `1970-01-01 00:00:01 UTC` até `2038-01-19 UTC`
- TIME: LIMITS={`-838:59:59` e `839:59:59`}
- YEAR: LIMITS={`1901` to `2155`}. Pode ser expresso no formato 2 ou 4 dígitos.

### 3.3 - Campos do tipo caracter.

### 3.3.1 - Caracteres

- CHAR(0-255): Cadeia de caracteres com valor fixo (de 0 a 256). O que falta é preenchido com espaços vazios.
- VARCHAR(0-255): Cadeia de caracteres com valor variável (de 0 a 256).

### 3.3.2 - Binários

- BINARY(0-255): Cadeia de caracteres com valor fixo (de 0 a 255). Expressos em binário.
- VARBINARY(0-255): Cadeia de caracteres com valor variável (de 0 a 255). Expressos em binário.

### 3.3.3 - blob (Binários longos)

É possível gravar um grande binário. Uma imagem ou um arquivo por exemplo.

- TINYBLOB: 255 bytes
- BLOB: 65.535 bytes
- MEDIUMBLOB: 16.777.215 bytes
- LONGBLOB: 4.294.967.295 bytes


### 3.3.4 - Campos do tipo Text

Usado para armazenar textos.

- TINYTEXT: 255 caracteres
- TEXT: 65.535 caracteres
- MEDIUMTEXT: 16.777.215 caracteres
- LONGTEXT: 4.294.967.295 caracteres


### 3.3.5 - Campos string do tipo ENUM

Permite armazenar uma lista pré-definida de valores.

**Exemplos**:

- ENUM('valor_1', 'valor_2', 'valor_3', 'valor_4')


### 3.3.6 - Atributos dos campos String

- SET e COLLATE:  Tipo de conjunto de caracteres serão suportados.

### 3.4 - Campos do tipo SPACIAL

- GEOMETRY
- POINT
- LINESTRING
- POLYGON

## 4 Operadores


Mysql Variables


    - Local: Created between the tags BEGIN and END.
    - Session: 
    - Global



### MySQL Functions



### MySQL Internals


