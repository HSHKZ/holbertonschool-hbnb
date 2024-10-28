from flask import Flask
from flask_jwt_extended import JWTManager
from .config import Config

jwt = JWTManager()

def create_app(config_object=Config):
    app = Flask(__name__)
    app.config.from_object(config_object)

    from .users import users_bp
    app.register_blueprint(users_bp)

    access_token = create_access_token(identity=user.id, additional_claims={"is_admin": user.is_admin})

    jwt.init_app(app)

    return app
