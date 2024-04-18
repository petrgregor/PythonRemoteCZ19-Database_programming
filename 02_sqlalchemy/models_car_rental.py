"""
Task 1

Create a car_rental database. Then create the tables cars, clients, bookings according to the guidelines (no relation yet):

    cars: car_id(int, pk), producer(str), model(str), year(int), horse_power(int), price_per_day(int)
    clients: client_id(int, pk), name(str), surname(str), address(str), city(str)
    bookings: booking_id(int, pk), client_id(int), car_id(int), start_date(date), end_date(date), total_amount(int)

"""
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Car(Base):
    __tablename__ = "cars"

    car_id = Column(Integer, primary_key=True, autoincrement=True)
    producer = Column(String(50), nullable=False)
    model = Column(String(50), nullable=False)
    year = Column(Integer, nullable=False)
    horse_power = Column(Integer, nullable=False)
    price_per_day = Column(Integer, nullable=False)

    def __str__(self):
        return f"<Car #{self.car_id}, {self.producer}>"


class Client(Base):
    __tablename__ = "clients"

    client_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    surname = Column(String(30), nullable=False)
    address = Column(String(50), nullable=False)
    city = Column(String(30), nullable=False)

    def __str__(self):
        return f"<Client #{self.client_id}: {self.name} {self.surname} {self.city}>"


class Booking(Base):
    __tablename__ = "bookings"

    booking_id = Column(Integer, primary_key=True, autoincrement=True)
    client_id = Column(Integer, nullable=False)
    car_id = Column(Integer, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    total_amount = Column(Integer, nullable=False)

    def __str__(self):
        return f"<Booking #{self.booking_id}: Client #{self.client_id} Car #{self.car_id}>"
