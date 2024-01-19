# ACID x BASE


## ACID Consistency Model

- Atomacity ou atomicidade
- Consistency ou consistência
- Isolation ou isolamento
- Durability ou durabilidade


- Garante que uma transação performada seja sempre consistente.
- Usada por instituições financeiras, data warehouses

- Databases que podem lidar com pequenas e simultâneas transações.
- Sistema totalmente consistente.
- Sempre usados para operações de transferência de dinheiro por instituições financeiras.



- BASE stands for Basically Available, Soft state and Eventually consistency

Focused on availability


NoSQL - Few requirements for immediate consistency, data freshness, and accuracy.
NoSQL Benefits: Availability, scale, and resilience.
Used by:
- Marketing and customer services companies
- Social media apps
World available online services

Favors availability over consistency of data
NoSQL databases use BASE consistency level
Fully available system.

Netflix, spotfy and uber uses 

Distributed Systems

- Collection of multiple interconnected databases
- Spread physically across various locations
- Data divided by:
    - fragmentation (partitioning, sharding)
    - replication (copy of data): Increases availability
- Base consistency model

Advantages of distributed systems:

- Reliability and availability
- Improved performance
Query

- Global reach

- Chalange about concurrency control => Concurrency of data
- Data is synchronized in the background
- Developer-driven consistency of data
- No support for transaction


## CAP Theorem

Consistency x Availability

- Early 2000s: emergence of hadoop, this first open big data architecture that allowed distributed storage and processing a large amount of data.
- Service emerging in 2000s required distributed databases;
    - Active and accessible worldwide
    - Always available
- Relational databases: ACID-based, relied data consistency
- Availability and consistency seemed impossible.

### CAP

- Consistency
- Availability
- Partition Tolerance: 
- Partition - a lost or temporarily delayed connection between nodes.

- Partition Tolerance: The cluster must work despite network issues.
- Distributed systems cannot avoid partitions and must be partition tolerant.
- Partition tolerance is a basic feature of NoSQL.

Partition Tolerance is a basic feature of NoSQL.
NoSQL: A choice between consistency and availability.

MongoDB: Choice consistency
Apache Cassandra: Choose availability


### Challenges in migrating RDBMS to NoSQL Databases

- NoSQL not a de factor replacement of RDBMS
- RDBMS and NoSQL cater to different use cases;
RDBMS to NoSQL should be done based on careful case-by-case analysis (need for performance? Flexibility)


#### RDBMS or NoSQL

RDBMS:
- Needs for full consistency
- Structured data (fixed schema)
- transactions
- Joins

NoSQL:
- High Performance
- Unstructured Data
- Availability
- Easy Scalability


#### Data driven model to query driven data model
- RDBMS: Starts from the data integrity, relations between entities.
- NoSQL: Starts from your queries, not from your data. Models based on the way applications interacts with the data

#### Normalized to denomalized data

- NoSQL: Think how data can be structured on your queries
- RDBMS: Start from your normalized data and then build the queries.

#### From ACID to BASE model

- Availability x Consistency
- CAP Theorem - Chose between availability and consistency

NoSQL systems, by design, do not support transactions and joins (except in limited cases)



## MongoDB


#### What is MongoDB Database?

- Document and NoSQL Database.
- Where data is structured in non relational way

#### What are documents?

- Associative arrays like JSON or Python dictionaries

#### What is a collection?

- A group of stored documents
- For example, all student records in Student section (collection).
- All staff records in Employees sections (collections).


#### What is a Database


#### MongoDB Datatypes

String, integers, doubles, booleans, lists, dictionaries, 

Why is MongoDB

- Model data as you read/write, not the other way
    - Traditional relational databases: Create schema first. Then create tables
    - To store another field, you have to alter tables;

- Bring structured/unstructured data
- High availability

Mongo is a popular choice of database for:

- large and unstructured.
- Complex.
- Flexible.
- Highly scalable applications.
- Self-managed, hybrid, or cloud hosted.

## Advantages of Mongodb

- Flexibility of schema
- Evolving Schema
- Code First Approach
- Querying using MQL
- Has a wide range of operators
for complex analysis

- High Availability
    - MongoDB is natively a high available system.
    - Resilient through redundancy.
    - No system maintenance downtime.
    - No upgrade downtime.

## Use cases of MongoDB

- IoT Devices:
    - Globally distributed devices
    - Fast responses.


- Ecommerce: Products with different attributes.

- Real-time Analytics:
    - Quick response to changes
    - Simplified ETL
    - Real time, along with operational

- Gaming
    - Globally scalable
    - No downtime
    - Support 

- Finance
    - Speed
    - Security
    - Reliability



## Mongo CRUD operations

Mongo Shell: command line tool that helps administrators interact with MongoDB

use database_name
show collections

### Create

**insertOne**: db.collection_name.insertOne({`document`})

returns:
- acknowledged: true,
- insertedId: ObjectID(`hash`)

**insertMany**: db.collection_name.insertMany([{`document_1`}, {`document_2`}])

returns:
- acknowledged: true,
- insertedId: ObjectID("hash)

**findOne**: db.collection_name.findOne({`last_name`: "doe"})

returns:
- acknowledged: true,
- insertedId: ObjectID("hash)

**findMany**: 

**replaceOne**

returns:
- acknowledged:
- matchedCount
- modifiedCount


**updateOne**
**updateMany**

**deleteOne**
**deleteOne**

**count**
**find**