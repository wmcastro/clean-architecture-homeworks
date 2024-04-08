from pymongo import MongoClient
 
class MongoDB(BaseDatos):
    def __init__(self, host, port, database):
        self.client = MongoClient(host, port)
        self.db = self.client[database]
        self.collection = self.db["collection"]
 
    def guardar(self, datos):
        self.collection.insert_one({"dato": datos})
 
    def leer(self):
        return [document["dato"] for document in self.collection.find()]