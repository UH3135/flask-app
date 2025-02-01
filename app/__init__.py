from flask import Flask
from app.models import db
from flask_wtf import CSRFProtect
from app.config import config
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__)

    env = os.getenv("FLASK_ENV", "default")
    app.config.from_object(config[env])
    csrf = CSRFProtect(app)
    
    # DB 설정
    db.init_app(app)

    with app.app_context():
        db.create_all()

    # BluePrint 설정
    from app.blueprints import register_blueprint
    register_blueprint(app)

    return app
