from flask import Flask
from .config import Config

def create_app(config_object=Config):
    app = Flask(__name__)
    app.config.from_object(config_object)

    # Import et enregistrement de routes ici (si nécessaire)
    # Exemple : from .views import main
    # app.register_blueprint(main)

    return app
