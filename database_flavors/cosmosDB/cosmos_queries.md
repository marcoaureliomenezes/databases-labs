The Azure Cosmos Db for NoSQL supports Structured Language (SQL) as a JSON query language.
In this module you will learn how to create efficient queries using the SQL query language.

After completing this module you'll be able to:

- Create and execute SQL query
- Project query results.
- Use built-in functions

## Undestand SQL query language

- Azure Cosmos DB for NoSQL uses the already popular query language (SQL) syntax to perform queries over semi-structured data. 
- If you have performed queries over semi-structured data. 
- If you have performed queries in database platform like MySQL or SQL Server, then you may already have some of the tools. 

For this module we will focus on a fictional container of products with the following structure:

- id: String | unique identifier
- CategoryId: String | Partition key
- CategoryName: String
- sku: String
- description: String
- price: Number
- tags: Array | [String id, String name]

A basic SQL query in Azure Cosmos DB for NoSQL would be similar to the same query in any other database platform; it would be composed of a few essential components:

    SELECT * FROM products

    SELECT 
        products.id,
        products.name,
        products.price,
        products.categoryName
    FROM
        products

One interesting caveat here's that it doesn't matter what name is used here for the source, as this will reference the source moving forward. You can think of this as a variable. It's uncommon to use a single letter from a container name

    SELECT
        p.name, 
        p.price
    FROM 
        p


We can also filter our queries using the WHERE keyword. In this example, we filter the list of products to those that have a price that is between $50 and $100

    SELECT
        p.name, 
        p.categoryName,
        p.price
    FROM 
        products p
    WHERE
        p.price >= 50 AND
        p.price <= 100

## Project query results

When developin


## implement Type-checking in queries

Up until now, we have had a sample data structure that is well-known and understood. But let's consider some possible exceptions. Each product item container has a property named tags. An array of objects in the container. Removing this assumption:

### Property tags is not defined

- First we can use the IS_DEFINE built-in function to check if the tags property exists at all in this item:

    SELECT
        IS_DEFINED(p.tags) AS tags_exist
    FROM
        products p

- Lets say that the tags property does exist, but it's not an array, it's another type of property. You can use IS_ARRAY built-in function to check if the tags property is an array.

    SELECT
        IS_ARRAY(p.tags) AS tags_is_array
    FROM
        products p

- We can also check if the tags property is null or not using IS_NULL built-in function.

    SELECT
        IS_NULL(p.tags) AS tags_is_null
    FROM
        products p

- There are even more built-in functions for different scenarios involving other data types.

For example, consider a situation where different data stores persist pricing information inconsistently. 
- Some persist pricing information using string data while others may store pricing information using numbers. 
The built-in IS_NUMBER or IS_STRING functions could be used in a WHERE expression of our queries.


    SELECT
        p.id,
        p.price, 
        (p.price * 1.25) AS priceWithTax
    FROM
        products p
    WHERE
        IS_NUMBER(p.price);


    SELECT
        p.id,
        p.price
    FROM
        products p
    WHERE
        IS_STRING(p.price)

## Some other Built-in Functions

The SQL query language for the Azure Cosmos DB for NoSQL with built-in functions for common tasks in a query. In this unit, we will walk trough a brief set of examples of those functions with:

- CONCAT(col_1 | str_1, col_2 | str_2, ...)
- LOWER(col_1 | str_1)
- GetCurrentDateTime()


## Execute queries in the SDK

The Microsoft.Azure.Cosmos.Container class in the SDK has a series of built-in classes to create a query, issue the query to Azure Cosmos DB for NoSQL, set up an asynchronous stream in C#, and return items efficiently back to the client.

The equivalent to: `SELECT * FROM products p` SQL
Is: QueryDefinition `query = new ("SELECT * FROM products p");` C#