"""
Task 1

Create a car_rental database. Then create the tables cars, clients, bookings according to the guidelines (no relation yet):

    cars: car_id(int, pk), producer(str), model(str), year(int), horse_power(int), price_per_day(int)
    clients: client_id(int, pk), name(str), surname(str), address(str), city(str)
    bookings: booking_id(int, pk), client_id(int), car_id(int), start_date(date), end_date(date), total_amount(int)

"""

from sqlalchemy import create_engine
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

Base.metadata.create_all(eng)
