from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.review import Review
from app.models.place import Place
from app import db

reviews_bp = Blueprint('reviews', __name__)

@reviews_bp.route('/api/v1/places/<int:place_id>/reviews', methods=['POST'])
@jwt_required()
def create_review(place_id):
    user_id = get_jwt_identity()
    place = Place.query.get(place_id)

    if place.owner_id == user_id:
        return jsonify({"error": "Cannot review your own place"}), 403

    # Vérifie si l'utilisateur a déjà posté une review pour ce lieu
    existing_review = Review.query.filter_by(place_id=place_id, author_id=user_id).first()
    if existing_review:
        return jsonify({"error": "Duplicate review"}), 400

    data = request.get_json()
    review = Review(content=data['content'], place_id=place_id, author_id=user_id)
    db.session.add(review)
    db.session.commit()
    return jsonify(review.to_dict()), 201
