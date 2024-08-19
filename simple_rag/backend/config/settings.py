from utils.credentials import get_mongodb_uri



def set_mongodb_config(app) -> None:
    """
    Set the MongoDB configuration for the Flask app
    """
    mongo_db_uri = get_mongodb_uri()
    
    app.config['MONGO_URI'] = mongo_db_uri
    
    
    