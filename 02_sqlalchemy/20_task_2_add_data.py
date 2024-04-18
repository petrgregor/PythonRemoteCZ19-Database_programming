"""
Task 2

Complete the clients and cars tables with the following data:

    clients: 'Andrzej', 'Nowak', 'ul. Saska 43', 'Wroclaw'
    cars: 'Seat', 'Leon', 2016, 80, 200

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

session.add(
    Client(name="Andrzej",
           surname="Nowak",
           address="ul. Saska 43",
           city="Wroclaw")
)

session.add(
    Car(producer="Seat",
        model="Leon",
        year=2016,
        horse_power=80,
        price_per_day=200)
)

session.commit()
