import os


BASE_DIR = os.path.dirname(__file__)

class Config():
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, "pybo.db")}"

class DevelopmentConfig(Config):
    FLASK_DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False