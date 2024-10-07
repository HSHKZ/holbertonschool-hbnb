import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_secret_key')
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
