# app/api/review_api.py
from flask import Blueprint, request, jsonify
from app.services.review_service import ReviewService

review_bp = Blueprint('review_bp', __name__)

@review_bp.route('/reviews', methods=['POST'])
def create_review():
    data = request.get_json()
    user_id = data.get('user_id')
    place_id = data.get('place_id')
    text = data.get('text')
    review = ReviewService.create_review(user_id, place_id, text)
    return jsonify(review), 201

@review_bp.route('/reviews/<int:review_id>', methods=['GET'])
def get_review(review_id):
    review = ReviewService.get_review(review_id)
    return jsonify(review) if review else ('', 404)

@review_bp.route('/reviews/<int:review_id>', methods=['PUT'])
def update_review(review_id):
    data = request.get_json()
    text = data.get('text')
    review = ReviewService.update_review(reviiew_id, text)
    return jsonify(review) if review else ('', 404)

@review_bp.route('/reviews/<int:review_id>', methods=['DELETE'])
def delete_review(review_id):
    review = ReviewService.delete_review(review_id)
    return ('', 204) if review else ('', 404)
