"""
Task 1

Create a car_rental database. Then create the tables cars, clients, bookings according to the guidelines (no relation yet):

    cars: car_id(int, pk), producer(str), model(str), year(int), horse_power(int), price_per_day(int)
    clients: client_id(int, pk), name(str), surname(str), address(str), city(str)
    bookings: booking_id(int, pk), client_id(int), car_id(int), start_date(date), end_date(date), total_amount(int)

"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Car(Base):
    __tablename__ = "cars"

    car_id = Column(Integer, primary_key=True, autoincrement=True)
    producer = Column(String(50))
    model = Column(String(50))
    year = Column(Integer)
    horse_power = Column(Integer)
    price_per_day = Column(Integer)

    def __str__(self):
        return f"<Car #{self.car_id}, {self.producer}>"



class Client(Base):
    # TODO Client
    pass


class Booking(Base):
    # TODO Booking
    pass