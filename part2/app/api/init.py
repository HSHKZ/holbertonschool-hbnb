# app/api/21.init.py

from flask import Flask
from flask_restx import Api
from app.api.user import user_ns
from app.api.amenity import amenity_ns
from app.api.place import place_ns

def create_app():
    app = Flask(__name__)
    api = Api(app, title='HBnB API', version='1.0', description='API for HBnB')

    # Enregistrement des namespaces
    api.add_namespace(user_ns, path='/api/v1/users')
    api.add_namespace(amenity_ns, path='/api/v1/amenities')
    api.add_namespace(place_ns, path='/api/v1/places')

    return app
