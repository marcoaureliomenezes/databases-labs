import uuid
import faker
from azure.identity import DefaultAzureCredential
from azure.cosmos import CosmosClient, PartitionKey
import urllib3
from random import randint, choice
import json

         

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def gen_fake_data():
    fake = faker.Faker(locale='pt_BR')
    type_row_2 = lambda: {
        'id': str(randint(1,10**6)), 
        'name': fake.name(),
        'age': str(fake.random_int(1, 98)),
        'tags': [{
            'id': str(randint(1,10**6)),
            'name': choice(['worn', 'apparel', 'no damage']),
            'class': choice(['trade-in', 'group'])
        } for i in range(3)]
    }
    return type_row_2()

if __name__ == "__main__":


    simulator_url = "https://127.0.0.1:8081/"
    cosmosdb_url = "https://dadaiacosmodb.documents.azure.com:443/"
    simulator_key = ("C2y6yDjf5/R+ob0N8A7Cgv30VRDJIWEHLM+4QDU5DE2nQ9nDuVTqobD4b8mGGyPMbIZnqyMsEcaGQy67XIw/Jw==")
    cosmosdb_key = "J3ZWbnxDTT5z25tjdcRVghogXYeGIvtYv6La3L4hNNwTR3KejuF2qUl9nr8H7Y94AngxKe5WJJE1ACDbftVeRA=="

    # Criar conexão com Database
    client = CosmosClient(url=simulator_url, credential=simulator_key, connection_verify=False)

    # Criar Database
    client.create_database_if_not_exists("dadaia_db")

    # Listar Databases
    list_databases = client.list_databases()

    # Criar Container dentro de Database dadaia_db
    dadaia_db = client.get_database_client("dadaia_db")
    dadaia_db.create_container_if_not_exists(id="prod_container", partition_key=PartitionKey(path="/id"))

    # Listar Containers dentro de Database dadaia_db
    list_containers = dadaia_db.list_containers()

    # Criar Item dentro de Container prod_container
    prod_container = dadaia_db.get_container_client("prod_container")
    for i in range(1):
        prod_container.create_item(gen_fake_data())

    pprint = lambda data: print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))
    # Listar Items dentro de Container prod_container -> Equivalente a SELECT * FROM container
    list_items = prod_container.read_all_items()
    data = [dict(i) for i in list_items]
    #print(pprint(data))



    # Query Items dentro de Container prod_container
    query_1 = "SELECT p.id, p.name, p.age, p.tags FROM p"
    items_1 = list(prod_container.query_items(query=query_1, enable_cross_partition_query=True))
    #print(pprint(items_1))

    
    # Join Items dentro de Container prod_container    
    query_2 = "SELECT p.id, p.name, t.name AS tags FROM products p JOIN t IN p.tags"
    items_2 = list(prod_container.query_items(query=query_2, enable_cross_partition_query=True))
    #print(pprint(items_2))
    #print("\n\n")


    query_3 = "SELECT VALUE t FROM t IN p.tags WHERE t.class = 'trade-in'"
    items_3 = list(prod_container.query_items(query=query_3, enable_cross_partition_query=True))
    #print(pprint(items_3))
    print("\n\n")

    query_4 = """
    SELECT p.id, p.name, t.name AS tags FROM products p JOIN
    (SELECT VALUE t FROM t IN p.tags WHERE t.class = 'trade-in') AS t
    """
    items_4 = list(prod_container.query_items(query=query_3, enable_cross_partition_query=True))
    #print(pprint(items_4))
    print("\n\n")

    query_5 = "SELECT p.name, t.name as tag FROM products p JOIN t IN p.tags WHERE p.price > 50"
    items_5 = list(prod_container.query_items(query=query_3, enable_cross_partition_query=True))
    print(pprint(items_5))


    dadaia_db.delete_container("prod_container")



