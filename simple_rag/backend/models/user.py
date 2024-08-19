from config.mongodb import mongo
from services.mongo_manager import insert_document

class UserModel:

    collection_name = "users"

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def to_document(self):
        return {
            "username": self.username,
            "password": self.password
        }

    def save_to_db(self):
        document = self.to_document()
        insert_document(collection_name= self.collection_name, document=document)

    @classmethod
    def find_by_username(cls, username):
        return mongo.db[cls.collection_name].find_one({"username": username})
        