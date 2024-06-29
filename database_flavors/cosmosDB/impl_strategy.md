## Request Units

- Each API has its own set of database operations. 
- These operations range from simple point reads and writes to complex queries.
- Each database operation consumes system resources based on the complexity of the operation.
- These system resources are expressed in terms of `Request Units (RUs)`, which is the `combination` of `CPU`, `IOPS`, `Memory`.
- `1 Request Unit` is the cost to do a point read for 1-KB item;
- Regardless of API, cost is always measured in RUs.
- RUs are available in each region associated with your Azure Cosmos DB account. You can't selectively assign RUs to a specific region.



First 1000 RU/s and 25 GB of storage for free.

## Throughput


- How many requests can be handled per second.
- Unit of Throughput: Request Unit (RUs).
- Each container is a unit of scalability for both throughput and storage.
- Users can provision throughput at either or both the database and container level.

If throughput is provisioned at the container level, that throughput value is reserved to that container.
If throughput is provisioned only at the Database level, all throughput are divided between the containers inside the database



## Cost Management

- Azure Cosmos DB capacity Calculator: http://cosmos.azure.com/capacitycalculator/
- Explore cost management tab.

## Partition and Partition Key

- A partition divides data in multiple chunks.
- Reduces IO in the Heap.
- 1 partition can't reside on Multiple machines.
- In 1 machine can reside multiple machines.



## Single and Cross Partition

Single partition query to get only 1 partition: Query performance is good.
Cross partition query Consumes lots of resources.

## Hot partition and query performance

- When use a partition key that is not distributed regularly. Data is not balanced.
- Users pay for the throughput provisioned. So Hot partitions are bad.
- Storage and queries also spread to different logical partitions.
- Amazon shopping cart eaxmple,
    - Partition Key bad choice: current timestamp
    - Partition key good choice: user id or product id.

## Time-to-live (TTL)

- Azure Cosmos DB allows you to set the length of time documents live in the database before being automatically purged.
- Measured in seconds from last modification.
- TTL can be defined on container as well as item level.
- Each document will be deleted after TTL.
- Data deletion is delayed if not enough RUs, consumes only leftover RUs.
- Data is not returned by any queries after TTL expired.

Why TTL:

- Automatic deletion of older data
- Enforce data retention policy
- Save cost.
- Improve performance
- Let us see how to configure TTL on portal


## Serveless

- Consumption-based model
- Eliminates the need to pre-provision throughput RUs ahead of time.

## Serverless x Provisioned Throughput

- Workloads: 
    - Predictable trrafic with minimal variance (provisioned throughput)
    - Varying traffic

- Request Units
    - Needs to provision throughput in advance ()
    - Doesn't require any planning or automatic provisioning.

- Global distribution
    - Supports unlimited number of azure regions
    - Can only run in a single Azure region

- Storage Limits:
    - Allows to store unlimited data in a container.
    - Allows up to 50 GB of data in a container.


## Autoscale x Standard Throughput

- Workloads
    - **Standard (Manual)**: Suited for workloads with steady traffic.
    - **Autoscale**: Better suited for unpredictable traffic.
    
- Request units
    - **Standard (Manual)**: Requires a static number of request units.
    - **Autoscale**: You only set the maximum, and the minimum billed will be 10% of the maximum when there are zero requests.

- Scenarios
    - **Standard (Manual)**: Ideal for scenarios where the full RU/s provisioned is consumed for > 66% of hours per month.
    - **Autoscale**: You only set the maximum, and the minimum billed will be 10% of the maximum when there are zero requests.