from pymongo import MongoClient

class Main:
    def __init__(self, host='localhost', port=27017, db_name='test'):
        self.client = MongoClient(host, port)
        self.db = self.client[db_name]

    def insert_document(self, collection_name, document):
        collection = self.db[collection_name]
        return collection.insert_one(document)

    def update_document(self, collection_name, query, new_values):
        collection = self.db[collection_name]
        return collection.update_many(query, {"$set": new_values})

    def replace_document(self, collection_name, query, document):
        collection = self.db[collection_name]
        return collection.replace_one(query, document)

    def delete_document(self, collection_name, query):
        collection = self.db[collection_name]
        return collection.delete_one(query)

    def find_documents(self, collection_name, query={}):
        collection = self.db[collection_name]
        return collection.find(query)

    def search_document(self, collection_name, query):
        collection = self.db[collection_name]
        return collection.find_one(query)

    def delete_all_documents(self, collection_name):
        collection = self.db[collection_name]
        return collection.delete_many({})

    def utility_operation1(self, collection_name):
        pass

    def utility_operation2(self, collection_name):
        pass