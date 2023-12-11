# models/restaurant.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models import Base

class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Integer)

    # Relationship with reviews
    reviews = relationship("Review", back_populates="restaurant")
    customers = relationship("Customer", secondary="reviews", back_populates="restaurants")


