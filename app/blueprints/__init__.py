from .main_view import main_bp
from .user_view import user_bp

def register_blueprint(app):
    app.register_blueprint(main_bp)
    app.register_blueprint(user_bp)