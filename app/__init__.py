from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import config
from dotenv import load_dotenv
import os

load_dotenv()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    env = os.getenv("FLASK_ENV", "default")
    app.config.from_object(config[env])
    
    # DB 설정
    db.init_app(app)

    with app.app_context():
        db.create_all()

    # BluePrint 설정
    from app.blueprints import register_blueprint
    register_blueprint(app)

    return app
