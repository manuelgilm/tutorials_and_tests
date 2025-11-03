import chromadb
from chromastart.utils import get_root_project
import os 
from dotenv import load_dotenv
from chromastart.utils import get_embeddings, get_openai_client
from datetime import datetime
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

def test2():
    load_dotenv()
    text = "this is a test text"
    client = get_openai_client()
    embedding = get_embeddings(openai_client = client, text=text)

    chroma_path = get_root_project() / "chromavs"

    if not os.path.exists(chroma_path):
        os.makedirs(chroma_path)

    ch_client = ch_client = chromadb.PersistentClient(chroma_path)
    collection = ch_client.create_collection(
        name="collection_with_emb_function2",
        embedding_function = OpenAIEmbeddingFunction(
            api_key = os.getenv("OPENAI_API_KEY"),
            model_name="text-embedding-ada-002"
        ),
        metadata = {
            "description": "My first chroma collection",
            "created": str(datetime.now())
        }
    )


def main() -> None:
    chroma_path = get_root_project() / "chromavs"

    if not os.path.exists(chroma_path):
        os.makedirs(chroma_path)

    ch_client = chromadb.PersistentClient(chroma_path)
    collection_name = "collection_with_emb_function2"
    collection = ch_client.get_collection(name=collection_name)
    if not collection:
        collection = ch_client.create_collection(name=collection_name)
    
    collection.add(
        ids=["id1","id2"],
        documents = [
            "This is a document about pineaple",
            "This is a document about orages"
        ]
    )

    results = collection.query(
        query_texts = ["This is a query document about hawaii"],
        n_results = 2
    )
    print(results)
    print(collection.name)
    print(collection.metadata)
    print(collection.configuration)