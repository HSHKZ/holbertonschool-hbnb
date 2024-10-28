class Config:
    SECRET_KEY = 'your_secret_key'
    DEBUG = False
    TESTING = False
    JWT_SECRET_KEY = 'your_jwt_secret_key'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
