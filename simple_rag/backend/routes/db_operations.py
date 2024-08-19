from flask import Blueprint 
from flask import request
from flask import jsonify
from config.mongodb import mongo
from services.mongo_manager import list_all_collections

collections = Blueprint('collections', __name__)

@collections.route('/list', methods=['GET'])
def list_collections():
    """
    List all the collections in the MongoDB database
    """
    return jsonify({"collections": list_all_collections()}), 200