# app/models/review_model.py
from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app import db

class Review(db.Model):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    place_id = Column(Integer, ForeignKey('places.id'), nullable=False)
    text = Column(String(500), nullable=False)
    created_at = Column(String(100), default=datetime.utcnow)
    updated_at = Column(String(100), default=datetime.utcnow)

    user = relationship("User", back_populates="reviews")
    place = relationship("Place", back_populates="reviews")
