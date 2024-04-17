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

# pro vložení jednoho záznamu
session.add(
    Student(first_name="Adéla", last_name="Becková")
)

# pro vložení více záznamů do databáze
session.add_all(
    [
        Student(first_name="Petr", last_name="Novák"),
        Student(first_name="Martin", last_name="Svoboda"),
        Student(first_name="Radek", last_name="Novotný"),
        Student(first_name="Lenka", last_name="Svobodová"),
        Student(first_name="Pavel", last_name="Strouhal"),
        Student(first_name="Pavla", last_name="Nováková")
    ]
)

session.commit()
