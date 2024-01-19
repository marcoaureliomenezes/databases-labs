from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, BulkWriteError, DuplicateKeyError
from faker_gen_data import gen_client


class MyMongoClient:

    def __init__(self, host, port, username, password):
        mongo_url = f'mongodb://{username}:{password}@{host}:{port}'
        self.mongo_client = MongoClient(mongo_url)

    def get_databases(self):
        return self.mongo_client.list_database_names()
    
    def create_database(self, database_name):
        self.mongo_client[database_name]

    def get_collections(self, database_name):
        db = self.mongo_client[database_name]
        return db.list_collection_names()

    def create_collection(self, database_name, collection_name):
        db = self.mongo_client[database_name]
        db[collection_name]

    def insert_one(self, database_name, collection_name, document):
        db = self.mongo_client[database_name]
        collection = db[collection_name]
        return collection.insert_one(document)

    def insert_many(self, database_name, collection_name, documents):
        db = self.mongo_client[database_name]
        collection = db[collection_name]
        return collection.insert_many(documents)

    def find_all(self, database_name, collection_name):
        db = self.mongo_client[database_name]
        collection = db[collection_name]
        return [i for i in collection.find({})]


if __name__ == '__main__':

    host = "127.0.0.1"
    port = "27017"
    username = "mongo"
    password = "mongo"
    database = 'test'

    mongo_client = MyMongoClient(host, port, username, password)

    print(mongo_client.get_databases())
    mongo_client.create_collection('test', 'clients')
    print(mongo_client.get_collections('test'))

    for i in range(1):
        insert_tx = mongo_client.insert_one('test', 'clients', gen_client())
        print(insert_tx.inserted_id, insert_tx.acknowledged)
    #print(mongo_client.find_all('test', 'my_test_collection'))


