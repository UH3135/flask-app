from flask import Blueprint

bp = Blueprint("main", __name__, url_prefix="/")

@bp.route("/")
def print_bp():
    return "this is blue print"