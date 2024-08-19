from flask import Blueprint
from flask import jsonify
from flask import request


from models.user import UserModel

users = Blueprint("users", __name__)


@users.route("/create", methods=["POST"])
def create_user():
    """
    Register a new user
    """
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    user = UserModel.find_by_username(username)
    if user:
        return jsonify({"message": "User already exists"}), 400

    user = UserModel(username, password)
    user.save_to_db()
    return jsonify({"message": "User registered successfully"}), 201


@users.route("/delete", methods=["DELETE"])
def delete_user():
    """
    Delete a user
    """
    data = request.get_json()
    username = data.get("username")
    user = UserModel.delete_user_from_db(username)
    if user:
        return jsonify({"message": "User deleted successfully"}), 200
    return jsonify({"message": "User not found"}), 404


@users.route("/get", methods=["GET"])
def get_user():
    """
    Get a user's details
    """
    data = request.get_json()
    username = data.get("username")
    user = UserModel.find_by_username(username)
    if user:
        user.pop("_id")
        return jsonify({"message": "User found", "data": user}), 200
    return jsonify({"message": "User not found"}), 404
