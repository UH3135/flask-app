from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

from config import DevelopmentConfig

# 다른 모듈에서 사용 가능하도록 구성
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    #ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    #blueprint
    from .views import main_view
    app.register_blueprint(main_view.bp)

    return app
