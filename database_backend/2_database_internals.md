## How tables and indexes are stored on Disk





## 1 - Database Internal Concepts:

### 1.1 - Table

- Logical set of rows and columns;

### 1.2 - Row_id

Internal and system maintained. In certain databases (mysql -innoDB) it is the same as the primary key but other databases, like Postgres have a system row_id (tuple_id).

### 1.3 - Page

- Depending on the Storage Model (row x column store), the rows are stored and read in logical pages.
- The database doesn't read a single row, it reads a page or more in a single IO and we get a lot of rows in that IO.
- Each page has a size (eg. 8KB in postgres, 16KB in MySQL).


### 1.4 - IO or Input/Output

- IO operation (input/output) is a read request to the disk.
- We try to minimize this as much as possible
- An IO can fetch 1 page or more depending on the disk partitions and other factors.
- An IO cannot read a single row, its a page with many rows in them, you get them for free.
- You want to minimize the number of IOs as they are expensive.
- Some IOs in operating systems goes to the operating system cache and not disk.

### 1.5 - Heap data structure

- The Heap is Data Structure where the table is stored with all its pages one after another.
- There is where the actual data is stored including everything.
- Trasversing the heap is expensive as we need to read so many data to find what we want.
- That is why we need indexes that help tell us exactly what part of heap we need to read. What pages of the Heap we need to pull.

### 1.6 - Index Data Structure b-tree

- An index is another data structure separate from the heap that has pointers to the heap.
- It has part of the data and used to quickly search for something.
- You can index on one column or more.
- Once you find a value of the index, you go to the heap to fetch more information where everything is there.
- Index tells you `exactly` which page to fetch in the heap instead of taking the hit to scan every page in the heap.
- The index is also stored as pages and cost IO to pull the entries of the index.
- The smaller the index, the more it can fit in memory the faster the search.
- Popular data structure for index is B-trees, learn more on that in the b-tree section.

### 1.7 - Notes

- Sometimes the heap table can be organized around a single index. This is called a clustered index or an Index Organized Table,
- Primary key is usually a clustered index unless therwise specified.
- MySQL InnoDB always have a primary key (clustered index) other indexes point to the primary key "value".
- Postgres only have a secondary indexes and all indexes point directly to the row_id which lives in the Heap.




## 2 - Row x Column Oriented Databases

- Row-oriented Database (Rows store)
- Column-Oriented Database (column Store)
- Pros & Cons


### 2.1 - Queries being analised

- No indexes
- SELECT first_name from employee WHERE ssn = 666;
- SELECT * FROM employee WHERE id = 1;
- SELECT SUM(salary) FROM employee;


### 2.2 - Row Oriented Database

- Tables are stored as rows in disk.
- Optimal for read/writes (OLTP - Online Transaction Processing).
- A single block IO read to the table fetches multiple rows with all their columns.
- More IOs are required to find a particular row in a table scan. However once you find the rows you get all columns for that row.
- Aggregation isn't efficient.
- Compression isn't efficient.
- Efficient queries.


- `SELECT * FROM employees WHERE snn == 666`
- `SELECT first_name FROM employees WHERE snn == 666` has the same number of IOs.
- `SELECT SUM(salary) FROM employee;` needs to scan all pages in Row Oriented Databases. Very inneficient.


### 2.2 - Column Oriented Database

- Tables are stored as columns first in disk.
- A single block IO read to the table fetches multiple columns with all matching rows.
- Less IOs are required to get more values of a given column. But working with multiple columns require more IOs.
- Optimal for read and summarize entire columns (OLAP - Online Analitical Processing).
- Deleting a Row can cause to scan all pages.
- Column Store databases don't do `SELECT *`.
- Writes are slow.
- Inefficient queries
- Amazing for aggregations.
- Amazing for compression.

- `SELECT first_name FROM employees WHERE snn == 666`: Very efficient. 1 IO to find ssn and 1 IO to fetch first_name value.
- `SELECT * FROM employees WHERE id == 1`: Very inefficient. n IOs for n pages.
- `SELECT SUM(salary) FROM employee;` 1 IO to find the column and aggregate. Very eficient.


**Observation**: Its possible to switch between Column oriented and Row Oriented changing the database engine.



### 2.3 - Primary Key x Secondary Key

Clustering: Organizing the table around a key, maintaining the order.
Primary Key or Clustered Indexes:

MySQL
Postgres
Oracle

Secondary Key: Table is a big mess and a separate structure exists called Index.