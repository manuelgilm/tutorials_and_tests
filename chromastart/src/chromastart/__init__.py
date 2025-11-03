import chromadb
from chromastart.utils import get_root_project
import os 

def main() -> None:
    chroma_path = get_root_project() / "chromavs"

    if not os.path.exists(chroma_path):
        os.makedirs(chroma_path)

    ch_client = chromadb.PersistentClient(chroma_path)
    collection_name = "my_collection"
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