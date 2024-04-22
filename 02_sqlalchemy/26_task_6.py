"""
Task 6

List the total cost of all bookings for each customer, customer name and surname
for bookings that were made between 10-17/07/2020.
"""

from sqlalchemy import create_engine, func
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

print("List the total cost of all bookings for each customer, customer name and surname "
      "for bookings that were made between 10-17/07/2020.")
query_result = (session.query(func.sum(Booking.total_amount), Client.name, Client.surname)
                .join(Client)
                .filter(Booking.start_date >= "2020-07-10", Booking.end_date <= "2020-07-17")
                .group_by(Client.client_id))
for result in query_result:
    print(result)

print("By name:")
query_result = (session.query(func.sum(Booking.total_amount), Client.name) #, Client.surname)
                .join(Client)
                .filter(Booking.start_date >= "2020-07-10", Booking.end_date <= "2020-07-17")
                .group_by(Client.name))
for result in query_result:
    print(result)
""" 
pymysql.err.OperationalError: 
(1055, 
"Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 
'car_rental.clients.surname' which is not functionally dependent on columns in GROUP BY clause; 
this is incompatible with sql_mode=only_full_group_by")
"""