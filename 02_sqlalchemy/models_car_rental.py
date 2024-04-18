"""
Task 1

Create a car_rental database. Then create the tables cars, clients, bookings according to the guidelines (no relation yet):

    cars: car_id(int, pk), producer(str), model(str), year(int), horse_power(int), price_per_day(int)
    clients: client_id(int, pk), name(str), surname(str), address(str), city(str)
    bookings: booking_id(int, pk), client_id(int), car_id(int), start_date(date), end_date(date), total_amount(int)

"""
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Car(Base):
    __tablename__ = "cars"

    car_id = Column(Integer, primary_key=True, autoincrement=True)
    producer = Column(String(50), nullable=False)
    model = Column(String(50), nullable=False)
    year = Column(Integer, nullable=False)
    horse_power = Column(Integer, nullable=False)
    price_per_day = Column(Integer, nullable=False)
    bookings = relationship("Booking", back_populates="car", cascade="all, delete", passive_deletes=True)

    def __repr__(self):
        return (f"<Car: id = {self.car_id}, "
                f"producer = {self.producer}, "
                f"model = {self.model}, "
                f"year = {self.year}, "
                f"horse_power = {self.horse_power}, "
                f"price_per_day = {self.price_per_day}>")


class Client(Base):
    __tablename__ = "clients"

    client_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    surname = Column(String(30), nullable=False)
    address = Column(String(50), nullable=False)
    city = Column(String(30), nullable=False)
    bookings = relationship("Booking", back_populates="client", cascade="all, delete", passive_deletes=True)

    def __repr__(self):
        return (f"<Client: id = {self.client_id}, "
                f"name = {self.name}, "
                f"surname = {self.surname}, "
                f"address = {self.address}, "
                f"city = {self.city}>")


class Booking(Base):
    __tablename__ = "bookings"

    booking_id = Column(Integer, primary_key=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey("clients.client_id", ondelete="CASCADE"), nullable=False)
    car_id = Column(Integer, ForeignKey("cars.car_id", ondelete="CASCADE"), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    total_amount = Column(Integer, nullable=False)
    car = relationship("Car", back_populates="bookings")
    client =relationship("Client", back_populates="bookings")

    def __repr__(self):
        return (f"<Booking: id = {self.booking_id}, "
                f"client_id = {self.client_id}, "
                f"car_id = {self.car_id}, "
                f"start_date = {self.start_date}, "
                f"end_date = {self.end_date}, "
                f"total_amount = {self.total_amount}>")
