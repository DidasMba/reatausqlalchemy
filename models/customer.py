# models/base.py
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()



from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    reviews = relationship('Review', back_populates='customer')
    restaurants = relationship('Restaurant', secondary='reviews', back_populates='customers')

    def full_name(self):
        # Implementation to return the full name of the customer
        pass

    def favorite_restaurant(self):
        # Implementation to find and return the favorite restaurant
        pass

    def add_review(self, restaurant, rating):
        # Implementation to add a new review
        pass

    def delete_reviews(self, restaurant):
        # Implementation to delete all reviews for a specific restaurant
        pass

