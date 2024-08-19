import os


def get_mongodb_uri() -> str:
    """
    Get the MongoDB URI from the environment variables
    """
    password = os.environ.get("MONGO_PASSWORD", None)
    username = os.environ.get("MONGO_USERNAME", None)
    db_name = os.environ.get("MONGO_DB_NAME", "test")

    if not password or not username:
        raise ValueError(
            "MongoDB username or password not found in environment variables"
        )

    mongo_uri = f"mongodb+srv://{username}:{password}@cluster0.hd6rj.mongodb.net/{db_name}?retryWrites=true&w=majority&appName=Cluster0"
    return mongo_uri   