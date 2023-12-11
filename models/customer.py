# models/customer.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models import Base

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)

    # Relationship with reviews
    reviews = relationship("Review", back_populates="customer")
    restaurants = relationship("Restaurant", secondary="reviews", back_populates="customers")

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def favorite_restaurant(self):
        # Implement logic to find the restaurant with the highest star rating
        pass

    def add_review(self, restaurant, rating):
        # Implement logic to add a review for the given restaurant with the specified rating
        pass

    def delete_reviews(self, restaurant):
        # Implement logic to delete all reviews for a specific restaurant
        pass

