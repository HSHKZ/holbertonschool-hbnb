from flask import Flask
from app.api.routes import api_blueprint

def create_app():
    app = Flask(__name__)
    
    # Enregistrement du blueprint pour l'API
    app.register_blueprint(api_blueprint, url_prefix='/api')
    
    return app
