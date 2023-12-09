from models import Restaurant, Customer, Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Configure your database connection
engine = create_engine('your_database_url')
Session = sessionmaker(bind=engine)
session = Session()

# Example usage
first_customer = session.query(Customer).first()
print(first_customer.restaurants)  # This should print a list of restaurants for the first customer

first_review = session.query(Review).first()
print(first_review.customer())  # This should print the customer for the first review
