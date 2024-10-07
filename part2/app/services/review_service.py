# app/services/review_service.py
from app.models.review_model import Review
from app import db

class ReviewService:
    @staticmethod
    def create_review(user_id, place_id, text):
        if not text:
            raise ValueError("Review text cannot be empty")
        review = Review(user_id=user_id, place_id=place_id, text=text)
        db.session.add(review)
        db.session.commit()
        return review

    @staticmethod
    def get_review(review_id):
        return Review.query.get(review_id)

    @staticmethod
    def update_review(review_id, text):
        review = Review.query.get(review_id)
        if review:
            review.text = text
            db.session.commit()
            return review
        return None

    @staticmethod
    def delete_review(review_id):
        review = Review.query.get(review_id)
        if review:
            db.session.delete(review)
            db.session.commit()
            return review
        return None
