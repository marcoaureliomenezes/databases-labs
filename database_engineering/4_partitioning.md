# Partitioning



## What is partitioning

- Split table in many partitions.
- Metadata about partitioning help query performance.
- Query works with a small set of data

## Horizontal Partitioning x Vertical Partitions


- Horizontal Partitioning splits rows into partitions
    - Range or list

- Vertical partitioning split columns partitions.
    - Large column (blob) that you can store in a slow access drive in its own table space.


## Partitioning Types

- By range
    - Dates, id (e.g. by logdate or customerid from to)

- By List
    - Discrete values (e.g. states CA, AL, etc.) or zip codes

- By hash
    - Hash functions (consistent hashing)


## Partitioning x Sharding

- HP splits big table into multiple tables in the same database, client is agnostic.
- Sharding spits big table into multiple tables across multiple database servers.
- HP table name changes (or schema).
- Sharding everything is the same but server changes.


## Pros of Partitioning

- Improves query performance when accessing a single partition;
- Sequential scan vs scattered index Scan;
- Easy Bulk Loading (attach partition);
- Archive old data that are barely accessed into cheap storage;

## Cons of Partitioning

- Updates that move rows from partition to another (slow or fail sometimes).
- Inneficient queries could accidently scan all partitions resulting in slower performance.
- Schema changes can be challeging (DBMS could manage it though).



## Potgres Partitions


- CREATE TABLE grades_org (id serial not null, g int not null);
- INSERT INTO grades_org(g) SELECT FLOOR(RANDOM()*100) FROM GENERATE_SERIES (0, 10000000);


- CREATE TABLE grades_part (id serial not null, g int not null);
- CREATE TABLE g0035 (like grades_parts including indexes);
- CREATE TABLE g3560 (like grades_parts including indexes);
- CREATE TABLE g6080 (like grades_parts including indexes);
- CREATE TABLE g80100 (like grades_parts including indexes);

- ALTER TABLE grades_part attach partition g0035 for values (0) to (35);
- ALTER TABLE grades_part attach partition g3560 for values (35) to (60);
- ALTER TABLE grades_part attach partition g6080 for values (60) to (80);
- ALTER TABLE grades_part attach partition g80100 for values (80) to (100);


- INSERT INTO grades_parts SELECT * FROM grades_org;

- CREATE INDEX grades_parts_idx ON grades_parts(g);

- EXPLAIN ANALYZE SELECT COUNT(*) FROM grades_parts WHERE g = 30;

- SELECT pg_relation_size(oid), relname FROM pg_class ORDER BY pg_relation_size(oid) DESC;
