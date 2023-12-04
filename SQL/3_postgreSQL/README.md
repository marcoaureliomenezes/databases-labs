


https://www.postgresql.org/docs/current/index.html



\l: Lista os databases

CREATE DATABASE database_name


## Data Types

**Reference**: https://www.postgresql.org/docs/current/datatype.html

Altera chaves de relacionamento

# Criando um relacionamento

CREATE TABLE `related_table` (
    id SERIAL,
    name VARCHAR(255),
    PRIMARY KEY (id)
);

CREATE TABLE `table` (
    `id` SERIAL,
    `fk_id` INTEGER,
    PRIMARY KEY (id),
    FOREIGN KEY (`fk_id`)
        REFERENCES `related_table` (`id`)
        ON DELETE ON `CASCADE | RESTRICT`
        ON UPDATE ON `CASCADE | RESTRICT`,
);