# seeds.py
from sqlalchemy.orm import Session
from models import Base, engine, SessionLocal
from models.restaurant import Restaurant
from models.customer import Customer
from models.review import Review

# Create tables
Base.metadata.create_all(bind=engine)

# Function to seed data
def seed_data(db: Session):
    # Add your sample data here
    pass

# Seed data
with SessionLocal() as db:
    seed_data(db)

