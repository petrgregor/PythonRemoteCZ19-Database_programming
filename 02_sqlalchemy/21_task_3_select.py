"""
Task 3

Check if the previously added data has been saved in the database -
add a piece of code that will list all the data
from the cars and clients tables.
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

print("List of clients:")
clients = session.query(Client).all()
for client in clients:
    print(client)

print("List of cars:")
cars = session.query(Car).all()
for car in cars:
    print(car)
