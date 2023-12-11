# models/review.py
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    star_rating = Column(Integer)

    # Foreign keys for relationships
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"))
    customer_id = Column(Integer, ForeignKey("customers.id"))

    # Relationships with Restaurant and Customer
    restaurant = relationship("Restaurant", back_populates="reviews")
    customer = relationship("Customer", back_populates="reviews")

    def full_review(self):
        return f"Review for {self.restaurant.name} by {self.customer.full_name()}: {self.star_rating} stars."
