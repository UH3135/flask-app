from flask import Blueprint, jsonify, request
from flask_wtf.csrf import generate_csrf


main_bp = Blueprint("main", __name__)

@main_bp.route("/csrf_token", methods=['GET'])
def get_csrf_token():
    token = generate_csrf()
    return jsonify({'csrf_token': token})