# app/api/init.py

from flask import Flask
from flask_restx import Api
from app.api.user import user_ns

def create_app():
    app = Flask(__name__)
    api = Api(app, title='HBnB API', version='1.0', description='API for managing users in HBnB')

    # Enregistrement du namespace pour les utilisateurs
    api.add_namespace(user_ns, path='/api/v1/users')

    return app
