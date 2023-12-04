

# Data Manipulation Language



## 1 - Criar banco de dados e tabelas

- CREATE DATABASE [IF NOT EXISTS] `database_name` | CREATE SCHEMA [IF NOT EXISTS] `database_name` [CREATION_SPECIFICATION] 

- DROP DATABASE [IF EXISTS] `database_name` | DROP SCHEMA [IF EXISTS] `database_name`

Option `CREATION_SPECIFICATION`:


- DEFAULT CHARACTER SET = `charset_name`
- DEFAULT COLLATE = `collation_name`
- DEFAULT ENCRYPTION = {`Y` | `N`}


CREATE [TEMPORARY] TABLE [IF NOT EXISTS] `table_name` [SCHEMA] [TABLE_OPTIONS] [PARTITIONS_OPTIONS]

Option `SCHEMA`:

## 2 - Alteração de schema de tabelas

- **Rename a table**: ALTER TABLE `table_name` RENAME `new_table_name`;
- **Rename a column of a table**: ALTER TABLE `table_name` RENAME COLUMN `old_name` TO `new_name`;
- **Modify column type of a table**: ALTER TABLE `table_name` MODIFY COLUMN `column_name` `new_col_type`;
- **Add constraints between tables**:
    - ALTER TABLE `table_name` ADD CONSTRAINT `constraint_name` FOREIGN KEY (`FK_col_name`) REFERENCES `referenced_table` (`PK_col_name`);

## N - Configurações

SET SQL_SAFE_UPDATES = {`0` | `1`};

## 3 - Inserção de dados em tabelas


### 3.1 - Inserindo linha com schema total

INSERT INTO `table_name` (`col_1`, `col_2`, `col_3`, `col_4`)
VALUES (`value_1`, `value_2`, `value_3`, `value_4`);


### 3.2 - Inserindo linha com schema parcial

INSERT INTO `table_name` (`col_1`, `col_2`, `col_3`, `col_4`)
VALUES (`value_1`, `value_2`, `value_3`, `value_4`);

### 3.3 - Inserindo varias linhas ao mesmo tempo

INSERT INTO `table_name` (`col_1`, `col_2`, `col_3`, `col_4`)
VALUES 
    (`value_1_1`, `value_1_2`, `value_1_3`, `value_1_4`),
    (`value_2_1`, `value_2_2`, `value_2_3`, `value_2_4`);


### 3.4 - Inserindo linhas lendo outra tabela


INSERT INTO `dst_table_name` SELECT * FROM `src_table_name` WHERE `condition`;

### 3.5 - Inserindo linhas importando dados de arquivos

Usa-se o Workbench


## 4 - Atualização de dados em tabelas

### 4.1 - Atualizando um único campo

UPDATE `table_name` SET `col_name` = `value` WHERE `condition_where_to_update`

### 4.2 - Atualizando mais de um campo

UPDATE `table_name` SET `col_name_1` = `value_1`, `col_name_2` = `value_2` WHERE `condition_where_to_update`

### 4.3 - Atualizando mais de uma linha

Depende somente da condição na cláusula WHERE.

UPDATE `table_name` SET `col_name` = `value` WHERE `condition_where_to_update`

### 4.4 - Atualizando usando UPDATE FROM

UPDATE `dst_table_name` a INNER JOIN `src_table_name` b ON `a.col_on_a` = `a.col_on_a` SET `a.col_to_set` = `b.value_to_set`;


## 5 - Deleção de dados em tabelas

DELETE FROM `table_name` WHERE `condition_where_to_update`


## 6 - COMMIT and ROLLBACK

**START TRANSACTION**:  Cria um ponto de estado do banco de dados.

**COMMIT**: Confirma todas as operações entre START TRANSACTION e o comando COMMIT. Persiste todos os INSERTs, UPDATEs e DELETEs.

**ROLLBACK**: Tudo que foi feito entre o START TRANSACTION e o comando ROLLBACK será desprezado e os dados voltarão ao status de quando o START TRANSACTION foi executado.


## 7 - Propriedade AUTO INCREMENT

- Usado em campos de primary key.

- Quando executamos o comando INSERT não é necessário especificar campos com a propriedade AUTO_INCREMENT.
- Pode-se ter apenas 1 camp AUTO_INCREMENT por tabela.
- Podemos forçar o novo valor do auto incremento durante um INSERT.


## 8 - Valores default para campos

É possível inserir valores padrões para campos na criação de tabelas.

Exemplo:

CREATE TABLE `table_name`
(
    `campo_id` INT AUTO_INCREMENT,
    `col_name_a` `col_type`,
    `col_name_b` `col_type` NULL,
    `col_name_c` `col_type` DEFAULT `default_value`,
    PRIMARY KEY(`campo_id`)
);


## 9 - Triggers

Um trigger (gatilho) é um tipo especial de stored procedure executado automaticamente quando ocorre um evento no servidor do banco de dados.

**Exemplo**: Ao incluir dados em uma tabela atualize um log com data e hora.


CREATE
    [DEFINER = user]
    TRIGGER `trigger_name`
    `trigger_time` `trigger_event`
    ON `tbl_name` FOR EACH ROW
    [`trigger_order`]
    `trigger_body`

**trigger_time**: { BEFORE | AFTER }
**trigger_event**: { INSERT | UPDATE | DELETE }
**trigger_order**: { FOLLOWS | PRECEDES } other `trigger_name`



## Stored Procedures











