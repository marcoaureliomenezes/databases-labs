# Database and Postgres Internals


## Heap

- **Heap**: É a estrutura de dados que armazena os dados de uma tabela.

- **Page**: É a unidade de armazenamento do Heap. Cada Page tem 8KB.


## Indexes

- **Index**: É uma estrutura de dados que permite a busca rápida de registros em uma tabela.

## Postgres

### Tipos de Scan


- **Sequencial Scan**: Faz a busca em todas as pages do Heap.
- **Index Scan**: Faz a busca em um Index.

## Bitmap Index Scan

- 1. Faz a busca no Index e monta um Bitmap contendo as pages co


## Partitioning

- **Partitioning**: É a técnica de dividir uma tabela em partes menores.

```sql

CREATE TABLE table_name (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    created_at TIMESTAMP
) PARTITION BY RANGE (created_at);

CREATE TABLE table_name_2021 PARTITION OF table_name FOR VALUES FROM ('2021-01-01') TO ('2022-01-01');
CREATE TABLE table_name_2022 PARTITION OF table_name FOR VALUES FROM ('2022-01-01') TO ('2023-01-01');

ALTER TABLE table_name ATTACH PARTITION table_name_2021;
ALTER TABLE table_name ATTACH PARTITION table_name_2022;


```
