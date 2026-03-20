import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///hbnb.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'super-secret-jwt-key')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://hbnb_user:hbnb_password@localhost/hbnb_db'

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
