import os


class Config:
    '''기본 설정(공통)'''
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    TEST = False


class DevelopmentConfig(Config):
    '''개발 환경'''
    SQLALCHEMY_DATABASE_URI = "sqlite:///dev.db"
    SECRET_KEY = 'dev-secret-key'  # 배포시에는 제거
    DEBUG = True


class ProductionConfig(Config):
    '''운영 환경 설정'''
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///prod.db")


config = {
    "default": DevelopmentConfig,
    "production": ProductionConfig,
    "development": DevelopmentConfig,
}
