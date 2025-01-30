from flask import Blueprint, jsonify, request


main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def hello_world():
    data = {"message": "hello!"}
    return jsonify(data)