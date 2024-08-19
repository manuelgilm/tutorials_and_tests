from flask import Blueprint 
from flask import jsonify 
from flask import request


from models.user import UserModel

users = Blueprint('users', __name__)

@users.route('/register', methods=['POST'])
def register_user():
    """
    Register a new user
    """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = UserModel(username, password)
    user.save_to_db()
    return jsonify({"message": "User registered successfully"}), 201