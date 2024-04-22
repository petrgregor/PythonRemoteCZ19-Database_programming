"""
Task 3

List all reservations for the client with id = 3. Try with both query () and select ().
"""

from sqlalchemy import create_engine, select
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

print("List all reservations for the client with id = 3 (query):")
query_result = session.query(Booking).filter(Booking.client_id == 3)
for booking in query_result:
    print(booking)

print("List all reservations for the client with id = 3 (select):")
conn = eng.connect()
query = select([Booking]).where(Booking.client_id == 3)
print(query)
query_result = conn.execute(query).fetchall()
for booking in query_result:
    print(booking)