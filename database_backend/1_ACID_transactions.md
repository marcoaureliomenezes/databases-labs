# Database Engineering
## 1 - ACID

**Database transaction**:

- A collection of queries;
- One unit of work;
- E.g: Deposit in a Account (SELECT, UPDATE, UPDATE);
- Transaction lifespan starts with a `BEGIN` and can end with a `COMMIT` or a `ROLLBACK`.
- Postgres: A lots of IO but the faster COMMIT.
- Transactions are used to change and modify data.
- Pecfectly normal to a read only transaction.

**What is ACID**:

### 1.1 - Atomacity

Critical concept in all kind of databases.

- All queries in a transaction must succeed.
- If one query fails, all prior successful queries in the transaction should rollback.
- If the database went down prior to a commit of a transaction, all the successful queries in the transaction should rollback.
- An atomic transaction is a transaction that will rollback all queries if one or more queries failed.

- **Consistency**: 


### 1.2 - Isolation

- Can my inflight transaction see changes made by other transactions that are also inflight?
- Read phenomena
    - **Dirty reads**: Can read transactions inflight, so maybe this transaction cannot be committed;
    - **Non-repeatable read**: A result given by a read is not repeatable
    - **Phantom reads**: Row
    - **Lost Updates**: 


#### 1.2.1 - Dirty Reads


Table Sales:

|PID       |QNT   |PRICE|
|----------|------|-----|
|Product 1 |10    | $5  |
|Product 2 |20    | $4  |

Dirty Reads example:
    TX1                                                 TX2

    BEGIN                                       
        SELECT PID, QNT * PRICE FROM SALES;
            Product 1, 50                               BEGIN
            Product 2, 80                                   UPDATE SALES SET QNT = QNT + 5 WHERE PID = 1;
        SELECT SUM(QNT*PRICE) AS PROFIT FROM SALES;
            PROFIT = 155
    COMMIT TX1
                                                        ROLLBACK TX2

**Conclusion**: We get $155 when it shoud be $130. We read a dirty value that has not been commited.

#### 1.2.2 - Non-repeatable Reads

Table Sales:

|PID       |QNT   |PRICE|
|----------|------|-----|
|Product 1 |10    | $5  |
|Product 2 |20    | $4  |

Dirty Reads example:

    TX1                                                 TX2

    BEGIN                                       
        SELECT PID, QNT * PRICE FROM SALES;                                 
            Product 1, 50                                   
            Product 2, 80
                                                        BEGIN
                                                            UPDATE SALES SET QNT = QNT + 5 WHERE PID = 1;
                                                        COMMIT TX2
        SELECT SUM(QNT*PRICE) AS PROFIT FROM SALES;
            PROFIT = 155
    COMMIT

**Conclusion**: We get $155 when it should be $130. We did read a committed value, but it gave us inconsistent results.


#### 1.2.3 - Phantom Reads

Table Sales:

|PID       |QNT   |PRICE|
|----------|------|-----|
|Product 1 |10    | $5  |
|Product 2 |20    | $4  |

Phantom reads example:

    TX1                                                 TX2

    BEGIN                                       
        SELECT PID, QNT * PRICE FROM SALES;                                 
            Product 1, 50                                   
            Product 2, 80
                                                        BEGIN
                                                            INSERT INTO SALES VALUES ('Product 3', 10, 1);
                                                        COMMIT TX2
        SELECT SUM(QNT*PRICE) AS PROFIT FROM SALES;
            PROFIT = 140
    COMMIT

#### 1.2.4 - Lost Updates

Table Sales:

|PID       |QNT   |PRICE|
|----------|------|-----|
|Product 1 |10    | $5  |
|Product 2 |20    | $4  |

Phantom reads example:

    TX1                                                 TX2

    BEGIN                                       
        UPDATE SALES SET QNT = QNT+10 WHERE PID=1                                 
                                                        BEGIN
                                                            UPDATE SALES SET QNT = QNT+5 WHERE PID=1
                                                        COMMIT TX2
        SELECT SUM(QNT*PRICE) AS PROFIT FROM SALES;
            PROFIT = 155
    COMMIT


**Conclusion**: We get $155 when it should be $180. Our update was overwritten another transaction and as result "lost".

- Isolation levels for inflight Transaction

- **Read uncommitted**: No isolation, any change from the outside is visible to the transaction, committed or not.
- **Read committed**: Each query in a transaction only sees committed changes by other transactions.
- **Repeatable Read**: The transaction will make sure that when a query reads a row, that row will remain unchanged the transaction while its running.
- **Snapshot**: Each query in a transaction only sees changes that have been committed up to the start of the transaction. It's like a snapshot.
- **Serializable**: Transactions are run as if they serialized one after the another. No parallelism.
version of the database at that moment.


Each DBMS implements Isolation level differenttly:

- **Pessimistic**: Row level locks, table locks, page locks to avoid lost updates.
- **Optimistic**: No locks, just track if things changed and fail the transaction if so.
- **Repeatable Read**: Locks the rows it reads but it could be expensive if you read a lot of rows, Postgres implements RR as snapshot. That is why you don't get phantom reads with Postgres in Repeatable Read.
- **Serializable**: Are usually implemented with optimistic concurrency control, you can implement it pessimistically with SELECT FOR UDPATE.


### 1.3 Consistency

- Consistency in Data - constraints
    - Defined by the user;
    - Referential integrity (foreign keys);
    - Atomicity
    - Isolation

- Consistency in reads - applies to the system as a whole
    - If a transaction committed a change will a new transaction immediately see the change?
    - Affects the system as a whole.
    - Relational and NoSQL databases suffer from this.
    - Eventual Consistency.

### 1.4 Durability

- Changes made by committed transactions must be persisted in a durable non-volatile storage.
- Durability techniques:
    - WAL - Write Ahead Log. Writing a lit of data to disk is expensive (indexes, data, files, columns, rows, etc). That is why DBMS persist a compressed version of the changes known as WAL.
    - Asynchronous snapshot.
    - AOF (Append Only Files)

    OS cache:

    - A Write request in OS usually goes to the OS cache.
    - When the  writes go the OS cache and OS crash, machine restart could lead to loss of data.
    - Fsync OS command forces writes to always go to disk.

    
When a transaction is commited the data is really recorded on hard disks.