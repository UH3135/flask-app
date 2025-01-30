from flask import Blueprint, jsonify, request
from app.models import User


user_bp = Blueprint("user", __name__)

@user_bp.route("/user", methods=["POST"])
def create_user():
    data = request.get_json()
    user = User(name=data['name'], email=data['email'])
    return jsonify({"id": user.id, "name": user.name, "email": user.email})


@user_bp.route("/user", methods=['GET'])
def get_user_by_id():
    users = User.get_all_users()
    return jsonify([{'id': user.id, 'name': user.name, 'email': user.email} for user in users])


@user_bp.route('/user', methods=['DELETE'])
def delete_user():
    name = request.get_json()['name']
    User.delete(name)
    return jsonify({'message': 'User deleted'})