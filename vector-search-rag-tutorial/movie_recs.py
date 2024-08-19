from utils import get_mongo_client
from utils import query_index
from dotenv import load_dotenv
import os

load_dotenv()

PASSWORD = os.getenv("PASSWORD")
HF_TOKEN = os.getenv("HF_TOKEN")

client = get_mongo_client(PASSWORD)

db = client.sample_mflix
collection = db.movies

query = {"inputs": "Imaginary characters from outer space at war"}

results = query_index(
    query=query, index_name="plotSemanticSearch", collection=collection
)

for document in results:
    print(f"Movie Name: {document['title']}, \n Plot: {document['plot']}\n")

# Code to embed the plots and store them in the collection
# for doc in collection.find({'plot': {'$exists': True}}).limit(5):
#     payload = {"inputs": doc['plot']}
#     embeddings = generate_embeddings(payload)
#     collection.update_one({'_id': doc['_id']}, {'$set': {'plot_embedding_hf': embeddings}})
