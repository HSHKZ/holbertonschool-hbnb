# app/api/init2.py

from flask import Flask
from flask_restx import Api
from app.api.user import user_ns
from app.api.amenity import amenity_ns

def create_app():
    app = Flask(__name__)
    api = Api(app, title='HBnB API', version='1.0', description='API for HBnB')

    # Enregistrement des namespaces pour utilisateurs et commodités
    api.add_namespace(user_ns, path='/api/v1/users')
    api.add_namespace(amenity_ns, path='/api/v1/amenities')

    return app
