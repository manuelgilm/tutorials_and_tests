from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
import requests
from typing import List


def get_mongo_client(passwsord: str) -> MongoClient:
    """
    Get a MongoClient object to connect to the MongoDB cluster.

    :param password: The password to connect to the MongoDB cluster.
    :return: A MongoClient object to connect to the MongoDB cluster.
    """

    uri = f"mongodb+srv://gil:{passwsord}@cluster0.hd6rj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi("1"))
    # Send a ping to confirm a successful connection
    try:
        client.admin.command("ping")
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    return client


def generate_embeddings(payload: str) -> List[float]:

    embedding_url = "https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2"

    HF_TOKEN = os.getenv("HF_TOKEN")
    response = requests.post(
        embedding_url,
        headers={"Authorization": f"Bearer {HF_TOKEN}"},
        json=payload,
    )

    if response.status_code != 200:
        raise Exception(
            f"Failed to generate embeddings: {response.status_code} : {response.text}"
        )

    return response.json()


def query_index(query: str, index_name: str, collection) -> List:
    """
    Query the index with the given query and return the results.

    :param query: The query to search for.
    :param index_name: The name of the index to query.
    :param collection: The collection to query.
    :return: The results of the query
    """

    results = collection.aggregate(
        [
            {
                "$vectorSearch": {
                    "queryVector": generate_embeddings(query),
                    "path": "plot_embedding_hf",
                    "numCandidates": 100,
                    "limit": 4,
                    "index": index_name,
                }
            }
        ]
    )

    return results
