from flask import Blueprint
from flask import request
from flask import jsonify

from models.user import UserModel

user = Blueprint("user", __name__)


@user.route("/user", methods=["POST"])
def create_user():
    user_data = request.get_json()
    user = UserModel.find_by_username(user_data["username"])
    if user:
        return jsonify({"message": "User already exists!"}), 400
    user = UserModel(**user_data)
    user.save_to_db()
    return jsonify({"message": "User created!"}), 201


@user.route("/user", methods=["PUT"])
def update_user():
    user_data = request.get_json()
    user = UserModel.find_by_username(user_data["username"])
    if not user:
        return jsonify({"message": "User not found!"}), 404

    new_username = user_data.get("new_username", None)
    if not new_username:
        return jsonify({"message": "New username is required!"}), 400

    user.username = user_data["new_username"]
    user.password = user_data["password"]
    user.save_to_db()
    return {"message": "User updated!"}


@user.route("/user", methods=["DELETE"])
def delete_user():
    user_data = request.get_json()
    user = UserModel.find_by_username(user_data["username"])
    if not user:
        return jsonify({"message": "User not found!"}), 404

    user.delete_from_db()
    return jsonify({"message": "User deleted!"}), 200


@user.route("/users", methods=["GET"])
def get_users():
    users = UserModel.query.all()
    users = [user.to_json() for user in users]
    return jsonify(users)


@user.route("/user", methods=["get"])
def get_user_by_username():
    user_data = request.get_json()
    user = UserModel.find_by_username(user_data["username"])
    if user:
        return jsonify(user.to_json()), 200

    else:
        return jsonify({"message": "User not found!"}), 404
