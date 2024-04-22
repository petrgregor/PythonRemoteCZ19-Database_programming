"""
Task 5

List the id of all customers and the booking costs incurred by them,
which are greater than 1100 and the bookings started after 13/07/2020 (>=14/07/2020).
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

print("List the id of all customers and the booking costs incurred by them, "
      "which are greater than 1100 and the bookings started after 13/07/2020 (>=14/07/2020).")
query_result = (session.query(Client.client_id, Booking.total_amount).join(Booking)
                .filter(Booking.total_amount > 1100, Booking.start_date >= "2020-07-14"))

for result in query_result:
    print(result)
