from config.mongodb import mongo

def list_all_collections():
    """
    List all the collections in the MongoDB database
    """
    return mongo.db.list_collection_names()

def insert_document(collection_name: str, document: dict):
    """
    Insert a document into a collection
    """
    mongo.db[collection_name].insert_one(document)