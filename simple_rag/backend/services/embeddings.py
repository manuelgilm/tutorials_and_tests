from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import MongoDBAtlasVectorSearch


def get_embeddings(text:str):
    """
    Get embeddings for a given text
    """
    return {"message": "Embeddings generated", "data": text}

def get_answer(query:str)->str:
    """
    Get answer for a given query
    """

    # get the embeddings for the query
    embeddings = get_embeddings(query)

    # get most relevant documents using the embeddings

    # pass the most relevant documents to the model alongside the query

    # get the answer from the model

    # return the answer
    return "This is the answer"

