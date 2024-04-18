"""
Task 3

List all reservations for the client with id = 3. Try with both query () and select ().
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models_car_rental import *

CONNECTION_STRING = "mysql+pymysql://{user}:{password}@{host}/{db}"

eng = create_engine(
    CONNECTION_STRING.format(
        user="test",
        password="test",
        host="localhost",
        db="car_rental"
    )
)

Session = sessionmaker(bind=eng)

session = Session()

print("List all reservations for the client with id = 3:")
query_result = session.query(Booking).filter(Booking.client_id == 3)
for booking in query_result:
    print(booking)
