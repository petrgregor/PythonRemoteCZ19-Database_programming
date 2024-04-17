from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student

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

# SELECT * FROM STUDENTS;
students = session.query(Student).all()
for student in students:
    print(student.get_full_name())

print("----")

total = session.query(Student).count()
print(f"Total: {total}")

print("----")
query_result = session.query(Student).filter(Student.id >= 3)
print("Found students with id >= 3:")
for row in query_result:
    print(row)

print("----")
query_result = session.query(Student).filter(Student.first_name.like("P%"))
print("Students with first name starting with P")
for row in query_result:
    print(row)

print("----")
query_result = session.query(Student).filter(Student.id >= 3, Student.first_name.like("P%"))
print("Students with id >= 3 and first name starting with P")
for row in query_result:
    print(row)
