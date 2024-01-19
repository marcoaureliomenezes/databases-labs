


## Ordem de comandos em uma query

- 1ª parte executada: FROM
- 2ª parte executada: WHERE
- 3ª parte executada: SELECT


## Operadores para condições na Cláusula WHERE

- Valor igual a: `SELECT * FROM table WHERE col_a = value_a`
- Valor diferente de: `SELECT * FROM table WHERE col_a <> value_a`
- Valor maior que: `SELECT * FROM table WHERE col_a > value_a`
- Valor maior ou igual a: `SELECT * FROM table WHERE col_a >= value_a`
- Valor menor que: `SELECT * FROM table WHERE col_a < value_a`
- Valor menor ou igual: `SELECT * FROM table WHERE col_a <= value_a`
- Valor contido em lista: `SELECT * FROM table WHERE col_a IN (value_a, value_b)`
- Valor não contido em lista: `SELECT * FROM table WHERE col_a IN (value_a, value_b)`
- Valor entre intervalo: `SELECT * FROM table WHERE col_a BETWEEN value_a AND value_b`


## Agrupamento de condições na cláusula WHERE

- Agrupamento de condição por OU: `SELECT * FROM table WHERE col_a = value_a OR col_b = value_b`
- Agrupamento de condição por OU: `SELECT * FROM table WHERE col_a = value_a AND col_b = value_b`




## Database Photo-Sharing

Tables:
- users
- photos
- comments
- likes



**3 Cenários de consistência para atualização**

**Situação:**

- ON DELETE RESTRICT: Retorna um erro.
- ON DELETE NO ACTION: Retorna um erro.
- ON DELETE CASCATE: Deleta linha de tabela alvo e linhas de tabelas relacionadas cujas chaves estrangeiras estão na tabela alvo.
- ON DELETE SET NULL Deleta linha de tabela alvo e atualiza linhas de tabelas relacionadas cujas chaves estrangeiras estão na tabela alvo com id NULL.
- ON DELETE SET DEFAULT

  





# Postgres Internals

### Heap ou Heap file

- todo dado relacionado com uma tabela
- Pode ser 


### Block ou Pages:

- Contém nenhuma ou muitas linhas ou tuplas ou items.
- Blocos de 8KB.

## Tuple: 

- Alias para Rows ou items

## Criação de INDEX no Postgres

Syntax: `CREATE INDEX ON table_name (column_name);`


**Default index name**: table_name_column_name_idx


## Query com EXPLAIN e EXPLAIN ANALYZE

Retorna informações sobre escaneamentos feitos para executar uma query.

Syntax: `EXPLAIN ANALYZE SELECT * FROM table_name WHERE column_name = value;`;

### Quando indexes não são eficientes?

- custo de storage: Indexes também são armazenados no storage.
- Indexes tornam operações de insert, update e delete mais lentas pois é preciso atualizar o index.
- Index pode não ser usado
- Não há garantia que vai indexes irão melhorar a performance do database.


### Comandos específicos do postgres para ver tamanho de tabela e index.

**do something**: `SELECT pg_size_pretty(pg_relation_size('users'));`
**do something**: `SELECT pg_size_pretty(pg_relation_size('users_username_idx'));`
**do something**: `SELECT pg_size_pretty(pg_relation_size('users'));`
**do something**: `SELECT pg_size_pretty(pg_relation_size('users_username_idx'));`
**do something**: `SELECT relname, relkind FROM pg_class WHERE relkind = 'i';`
**do something**: `CREATE EXTENSION IF NOT EXISTS pageinspect;`
**do something**: `SELECT * FROM bt_metap('users_username_idx');`
**do something**: `SELECT * FROM bt_page_items('users_username_idx', 3);`
**do something**: `SELECT * FROM bt_page_items('users_username_idx', 1);`
**do something**: `SELECT * FROM bt_page_items('users_username_idx', 2);`
**do something**: `SELECT ctid, * FROM users WHERE username = 'Aaliyah.Hintz';`
**do something**: `SELECT oid, datname FROM pg_database;`
**do something**: `SHOW data_directory;`


## Tipos de Indexes

- B-Tree: General purpose index, 99% of time you want this
- Hash: Speed up equality checks
- GiST: Geometry, Full text search
- SP-GiST: Clustered data, such as dates many rows might have same year.
- GIN: For columns that contains arrais or JSON data
- BRIN: Specialized for really large datasets.


**OBS**: Chaves primárias e colunas restritas como únicas possuem automaticamente indexes.


Default indexes are not showed inside indexes.


### Behind the scenes Indexes

8KB pages

- Meta Page (Metadata about the index)
- Leaf pages
- Root Page

1 comparação para descer um nó.
Complexidade = profundidade




## EXPLAIN e EXPLAIN ANALYZE

simbolo '->' Query nodes: Busca dados


Sequential Scan: 
Hash
Hash JOIN

Seq Scan on comments


### Fetch all comments (Seq Scan)

- Para page in [page_1, page_n]:
    - Open the heap file;
    - Load all comments;
    - Process each comment in some way;

    Reapeat the process for the nex block


`num_table_pages` x  `factor_weight_to_fetch_1_page_from_disk` + `num_rows_inside_page` x `factor_weight_to_process_rows_in_memory)`


### What influences Cost


- num_pages_read_sequencially x seq_page_cost (Seq read)
- num_pages_reat_at_random x random_page_cost
- num_rows_scanned x cpu_tuple_cost  (Seq read)
- num_entries_scanned x cpu_index_tuple_cost -> 0
- num_times_function_or_operator_evaluated x cpu_operator_cost -> 0


https://postgresql.org.docs/current/runtime-config-query.html

4 * 4 + 20 * 1 + 75 * 0.005 + 214 * 0.01

Hash Join (cost(=8.31..1756.11 rows=11 width=81))

Example:

- num_ages x 1 + num_rows_inside_page x 0.01


Query SELECT * FROM users WHERE username = 'Alyson14';

Parser (Query Tree) -> Rewriter (Decompose views) -> Planner (Query Plan) -> Executor

Query Tree

**EXPLAIN** Build a query plan and display info about it.
**EXPLAIN ANALYZE**: Build a query plan, run it, and info about it.




## SQL for Postgres

SELECT * FROM pg_database;

SELECT * FROM information_schema.tables WHERE table_schema = 'public';


Execute Postgres CLI from docker container:

    $ docker exec -it {container_name} psql -U postgres


    # INSERT INTO temp (t) SELECT RANDOM() * 100 FROM GENERATE_SERIES(0,1000000);

    #1 EXPLAIN ANALYZE SELECT id FROM employees WHERE id = 2000; Faster
    #2 EXPLAIN ANALYZE SELECT name FROM employees WHERE id = 3000; Faster like #1
    #3 EXPLAIN ANALYZE SELECT id FROM employees WHERE name = 'Zn'; Slow
    #4 EXPLAIN ANALYZE SELECT id FROM employees WHERE name LIKE '%Zn%'; Slow


    #5 CREATE INDEX employees_name ON employees(name);

    #6 EXPLAIN ANALYZE SELECT id FROM employees WHERE name = 'Zn'; Faster than query #3 an #4
    #7 EXPLAIN ANALYZE SELECT id FROM employees WHERE name = 'Zn'; Slower like #4


## EXPLAIN command

EXPLAIN SELECT * FROM grades;

- Sequential Scan
- Cost: `time_first_page`..`time_last_page`
- Rows: Number of rows. E.g: Estimation of number of Rows.
- Width: number of Bytes of the selected columns


EXPLAIN SELECT * FROM grades ORDER BY name;

EXPLAIN SELECT ID FROM grades; Width of columns (data type sizes)



## Sequential table Scan

EXPLAIN SELECT name FROM grades WHERE id = 1000;

## Sequential Index Scan

## Bitmap Scan

## Difference Key x Non-key column indexes

## Difference between Index Scan and Index Only Scan

EXPLAIN SELECT name FROM grades WHERE id = 7;

CREATE INDEX id_idx ON grades(id);

EXPLAIN SELECT name FROM grades WHERE id = 7; Index Scan

EXPLAIN SELECT id FROM grades WHERE id = 7; Index Only Scan

DROP INDEX id_idx;

CREATE INDEX id_idx ON grades (id) include (name)

EXPLAIN SELECT name FROM grades WHERE id = 7; Index Only Scan

EXPLAIN SELECT * FROM grades WHERE id = 7;


Index Scan: Vai no index e no Heap.
Index Only Scan: Vai somente no index.



# CTEs Common Table Expressions


# Recursive CTEs

Useful anytime you have a tree or a graph-type data structure

Most use a union keyword - simple CTE don't have to use a union

This super, super advanced. Don't expect to be able write your own recursive CTE's. Just that they exist.
