"""
Task 7

Write query stm in SQL and pass it to the query () function.
stm should return the id of reservations for which the reservation value is greater
than the value given to the main query as a parameter.
"""

from sqlalchemy import create_engine, func, text
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

print("Write query stm in SQL and pass it to the query () function. "
      "stm should return the id of reservations for which the reservation value is greater "
      "than the value given to the main query as a parameter.")

amount = int(input("Zadete částku: "))
stm = text("SELECT booking_id FROM bookings WHERE total_amount > :amount")
query_result = session.query(Booking).from_statement(stm).params(amount=amount)
for result in query_result:
    print(result)
