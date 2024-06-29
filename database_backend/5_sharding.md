# Sharding


## O que é Sharding

### Necessidade

- Divisão de linhas da tabela para diferentes servidores mesmo schema.
- Sharding rules


## Consistent Hashing

- A partir de uma entrada é possivel escolher qual servidor será requisitado.
- Localização de registro é escolhida a partir de `Hash(coluna) % num_servers`
- Escolha de qual da

## Horizontal partitions x Sharding

- HP split big table into tables in the same database
- Sharding splits big tables into multiple tables across multiple database servers;
- HP table name changes (or schema)
- Sharding everything is the same but server changes

## Example (code with Postgres)


- Spin up 3 postgres instances with identical schema 5432, 5433, 5434
- Write to the sharded databases;
- Reads from the sharded databases;

init.sql

    CREATE TABLE URL_TABLE (id serial NOT NULL PRIMARY KEY, URL text, URL_ID character(5))

Dockerfile

    FROM postgres
    COPY init.sql /docker-entrypoint-initdb.d

Pros and Cons