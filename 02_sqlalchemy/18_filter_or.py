from sqlalchemy import create_engine, or_, and_
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

print("vypsat všechny studenty, jejichž jméno začíná na P nebo R")
query_result = session.query(Student).filter(or_(Student.first_name.like("P%"), Student.first_name.like("R%")))
for row in query_result:
    print(row)

print('vypsat všechny studenty se jménem "Petr" a "Martin"')
query_result = session.query(Student).filter(Student.first_name.in_(["Petr", "Martin"]))
for row in query_result:
    print(row)