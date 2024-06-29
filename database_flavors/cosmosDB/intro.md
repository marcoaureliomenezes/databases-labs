# Configure the Azure Cosmos DB for NoSQL SDK

Often users will need to configure the Azure Cosmos DB for NoSQL SDK for .NET to enable:

- common scenarios,
- troubleshoot problems, 
- improve performance,
- gather deeper insight.

The SDK includes a rich set of options, along with a fluent builder, to configure your applications to perform and be managed in a way that is useful to your team.

After completing this module you'll be able to:

- Configure the SDK for offline development.
- Troubleshoot common connection errors.
- Implement parallelism in the SDK.
- Configure logging using the SDK.

## Enabling offline development

As you begin to use Azure Cosmos DB across multiple projects, there will be eventually a need to use and test Azure Cosmos DB in a local environment where you can validate new code  quickly without creating a new instance in the Cloud. 
The Azure Cosmos DB emulator is a great tool for common Dev+ Test workflows that developers may need to implement on their local machine.


### Azure Cosmos DB emulator

The Azure Cosmos DB emulator is a local environment that is useful to develop and test applications without incurring the costs or complexity of an Azure Subscription.

Emulator is available to run on Windows, Linux or Docker container image.

    docker pull mcr.microsoft.com/cosmosdb/linux/azure-cosmos-emulator

### Configuring the SDK to connect to the emulator

The Azure Cosmos DB emulator uses the same APIs as the cloud service. The emulator uses a single fixed account with a static authentication key that is the same across all instances.

    string endpoint = "https://localhost:8081/";
    string key = "C2y6yDjf5/R+ob0N8A7Cgv30VRDJIWEHLM+4QDU5DE2nQ9nDuVTqobD4b8mGGyPMbIZnqyMsEcaGQy67XIw/Jw==";
    CosmosClient client = new (endpoint, key);


### Handle connection errors

While most of your requests are fine, there are some scenarios where a request can fail for a temporary reason. In these scenarios, it's both normal and expected for you to retry the request after a reasonable amount of time.

429: Too many requests;
449: concurrency error;
500: Unexpected service error;
503: Service unavailable;

There are HTTP error codes, such as 400 (bad request), 401 (not authorized); 403 (forbidden) and 404 (not found) that indicate a failure client-side that should be fixed in application code and not retried.

### Implementing Threading and parallelism

While the SDK implements thread-safe types and some of parallelism, there are best practices that you can implement in your application code to ensure that the SDK has the best performance it can have in your workload.

### Avoid resource-related timeouts

Many times request timeouts occur due  high CPU or port utilization on client machine rather than a server-side issue. It's important to monitor resource utilization on client machines and scale-out appropriately to avoid SDK errors or retries due to local resource exhaustion.

### Use async/await in .NET

    Database database = await client.CreateDatabaseIfNotExistsAsync("cosmicworks");

## Configure max concurrency, parallelism, and buffered item count

When issuing a query from SDK, the QueryRequestOptions include a set of properties to tune a query's performance.

### Max item count

- All query results in Azure Cosmos DB for NoSQL are returned as "pages" of results. 
- This property indicates the number of items you would like to return in each "page".
- The service default is 100. You can set this value to -1 to set a dynamic page size.
- In this example below the MaxItemCount property is set to a value of 500.

    QueryRequestOptions options = new ()
    {
        MaxItemCount = 500
    };

OBS: If you use a MaxItemCount of -1, you should ensure the total response doesn't exceed the service limit for response size. For instance, the max response size is 4MB.

### Max concurrency

- `MaxConcurrency` specifies the number of concurrent operations ran client side during parallel query execution
- If set to 1, parallelism is effectively disable.
- If set to -1, the SDK manages this setting. 
- Ideally, users would set this value to the number of physical partitions for your container.
- Example below sets MaxConcurrency property to a value of 5;

    QueryRequestOptions options = new ()
    {
        MaxConcurrency = 5
    };

### Max Buffered Item Count

- The `MaxBufferedItemCount` property sets the maximum number of items that are buffered client-side during a parallel execution. 
- If set to -1, the SDK manages this settings.
- The ideal value for this setting will largely depend on the characteristics of your client machine.
- The example below the MaxBufferedItemCount property is set to a value of 5000.

    QueryRequestOptions options = new ()
    {
        MaxBufferedItemCount = 5000
    };


