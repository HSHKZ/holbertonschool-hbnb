# app/api/36.place.py

from flask import request
from flask_restx import Namespace, Resource, fields
from app.services.place_service import PlaceService

place_ns = Namespace('places', description='Place management operations')

# Modèles pour la validation des données
place_model = place_ns.model('Place', {
    'id': fields.String(readOnly=True, description='The place unique identifier'),
    'name': fields.String(required=True, description='The place name'),
    'price': fields.Float(required=True, description='The price per night'),
    'latitude': fields.Float(required=True, description='The latitude of the place'),
    'longitude': fields.Float(required=True, description='The longitude of the place'),
    'owner_id': fields.String(required=True, description='The owner ID')
})

place_create_model = place_ns.model('PlaceCreate', {
    'name': fields.String(required=True, description='The place name'),
    'price': fields.Float(required=True, description='The price per night'),
    'latitude': fields.Float(required=True, description='The latitude of the place'),
    'longitude': fields.Float(required=True, description='The longitude of the place'),
    'owner_id': fields.String(required=True, description='The owner ID')
})

place_update_model = place_ns.model('PlaceUpdate', {
    'name': fields.String(description='The place name'),
    'price': fields.Float(description='The price per night'),
    'latitude': fields.Float(description='The latitude of the place'),
    'longitude': fields.Float(description='The longitude of the place'),
})

@place_ns.route('/')
class PlaceList(Resource):
    @place_ns.marshal_list_with(place_model)
    def get(self):
        """Retrieve a list of all places"""
        return PlaceService.get_all_places(), 200

    @place_ns.expect(place_create_model)
    @place_ns.marshal_with(place_model, code=201)
    def post(self):
        """Create a new place"""
        data = request.json
        return PlaceService.create_place(data), 201

@place_ns.route('/<string:place_id>')
class Place(Resource):
    @place_ns.marshal_with(place_model)
    def get(self, place_id):
        """Retrieve a place by ID"""
        place = PlaceService.get_place_by_id(place_id)
        if place:
            return place, 200
        place_ns.abort(404, "Place not found")

    @place_ns.expect(place_update_model)
    @place_ns.marshal_with(place_model)
    def put(self, place_id):
        """Update a place"""
        data = request.json
        place = PlaceService.update_place(place_id, data)
        if place:
            return place, 200
        place_ns.abort(404, "Place not found")
