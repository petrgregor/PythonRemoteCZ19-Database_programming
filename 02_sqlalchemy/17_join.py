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

query_result = session.query(Student, Locker).join(Locker)
for row in query_result:
    student, locker = row
    print(f"Student {student} has locker {locker}")

print("------")
query_result = session.query(Student, Locker).join(Locker).filter(Locker.number > 10)
for row in query_result:
    student, locker = row
    print(f"Student {student} has locker {locker}")
