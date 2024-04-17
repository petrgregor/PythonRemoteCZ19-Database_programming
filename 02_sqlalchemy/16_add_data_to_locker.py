from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
from models import Base, Student, Locker

#                   dialect+driver://username:password@host:port/database
CONNECTION_STRING = "mysql+pymysql://{user}:{password}@{host}/{db}"

eng = create_engine(
    CONNECTION_STRING.format(
        user="test",
        password="test",
        host="localhost",
        db="school"
    )
)

Session = sessionmaker(bind=eng)

session = Session()

# pokud se snažíme pracovat s neexistujícím záznamem, skončíme s chybou
try:
    session.add(Locker(number=15, student=10))  # IntegrityError
    session.commit()
except IntegrityError:
    session.rollback()
    print("Error")

try:
    session.add_all(
        [
            Locker(number=15, student=1),
            Locker(number=20, student=2),
            Locker(number=4, student=3),
            Locker(number=5, student=4),
            Locker(number=3, student=5),
            Locker(number=17, student=6),
            Locker(number=21, student=7)
        ]
    )
    session.commit()
except IntegrityError:
    session.rollback()
    print("Error2")

