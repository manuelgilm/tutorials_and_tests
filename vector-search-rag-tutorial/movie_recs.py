from utils import get_mongo_client
from utils import generate_embeddings
from dotenv import load_dotenv
import os

import requests

load_dotenv()

PASSWORD = os.getenv("PASSWORD")
HF_TOKEN = os.getenv("HF_TOKEN")

client = get_mongo_client(PASSWORD)

db = client.sample_mflix
collection = db.movies

for doc in collection.find({'plot': {'$exists': True}}).limit(5):
    payload = {"inputs": doc['plot']}
    embeddings = generate_embeddings(payload)
    collection.update_one({'_id': doc['_id']}, {'$set': {'plot_embedding_hf': embeddings}})
    