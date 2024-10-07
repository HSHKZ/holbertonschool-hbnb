# app/api/amenity.py

from flask import request
from flask_restx import Namespace, Resource, fields
from app.services.amenity_service import AmenityService

amenity_ns = Namespace('amenities', description='Amenity management operations')

# Modèles pour la validation des données
amenity_model = amenity_ns.model('Amenity', {
    'id': fields.String(readOnly=True, description='The amenity unique identifier'),
    'name': fields.String(required=True, description='The amenity name')
})

amenity_create_model = amenity_ns.model('AmenityCreate', {
    'name': fields.String(required=True, description='The amenity name')
})

amenity_update_model = amenity_ns.model('AmenityUpdate', {
    'name': fields.String(description='The amenity name')
})

@amenity_ns.route('/')
class AmenityList(Resource):
    @amenity_ns.marshal_list_with(amenity_model)
    def get(self):
        """Retrieve a list of all amenities"""
        return AmenityService.get_all_amenities(), 200

    @amenity_ns.expect(amenity_create_model)
    @amenity_ns.marshal_with(amenity_model, code=201)
    def post(self):
        """Create a new amenity"""
        data = request.json
        return AmenityService.create_amenity(data), 201

@amenity_ns.route('/<string:amenity_id>')
class Amenity(Resource):
    @amenity_ns.marshal_with(amenity_model)
    def get(self, amenity_id):
        """Retrieve an amenity by ID"""
        amenity = AmenityService.get_amenity_by_id(amenity_id)
        if amenity:
            return amenity, 200
        amenity_ns.abort(404, "Amenity not found")

    @amenity_ns.expect(amenity_update_model)
    @amenity_ns.marshal_with(amenity_model)
    def put(self, amenity_id):
        """Update an amenity"""
        data = request.json
        amenity = AmenityService.update_amenity(amenity_id, data)
        if amenity:
            return amenity, 200
        amenity_ns.abort(404, "Amenity not found")
