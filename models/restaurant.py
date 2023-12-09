# models/base.py
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()



from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

    reviews = relationship('Review', back_populates='restaurant')
    customers = relationship('Customer', secondary='reviews', back_populates='restaurants')

    @classmethod
    def fanciest(cls):
        # Implementation to find and return the fanciest restaurant
        pass

    def all_reviews(self):
        # Implementation to get all reviews for this restaurant
        pass
