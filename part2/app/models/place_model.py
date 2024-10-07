# app/models/place_model.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app import db

class Place(db.Model):
    __tablename__ = 'places'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(500), nullable=True)

    reviews = relationship("Review", back_populates="place")
