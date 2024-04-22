"""
Task 4

List all cars rented by the customer with id = 5. Cars can repeat themselves, we mean the rental history.
Try with both query () and select ().
"""

from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker, join
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

print("List all cars rented by the customer with id = 5. (query)")
query_result = session.query(Booking).filter(Booking.client_id == 5)
for booking in query_result:
    print(booking.car)

print("-------------")
bookings = session.query(Booking).filter_by(client_id=5)
for booking in bookings:
    print(booking.car)

print("-------------")
clients = session.query(Client).filter_by(client_id=5)  # seznam obsahující jeden objekt
for client in clients:
    for booking in client.bookings:
        print(booking.car)

print("-------------")
client = session.query(Client).filter_by(client_id=5).first()  # maximálně jeden objekt (není seznam)
if client:
    for booking in client.bookings:
        print(booking.car)

print("List all cars rented by the customer with id = 5. (select)")
subquery = join(Booking, Car, Booking.car_id == Car.car_id)
query = select([Car]).select_from(subquery).where(Booking.client_id == 5)
print(query)
conn = eng.connect()
query_result = conn.execute(query).fetchall()
#print(query_result)
for car in query_result:
    print(car)
