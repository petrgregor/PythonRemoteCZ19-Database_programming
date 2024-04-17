from sqlalchemy import create_engine
from models import Base, Student

#                   dialect+driver://username:password@host:port/database
CONNECTION_STRING = "mysql+pymysql://{user}:{password}@{host}/{db}"
# CONNECTION_STRING = "mysql+mysqlconnector://{user}:{password}@{host}/{db}"

eng = create_engine(
    CONNECTION_STRING.format(
        user="test",
        password="test",
        host="localhost",
        db="school"
    )
)
#eng = create_engine("mysql+pymysql://test:test@localhost/school")

Base.metadata.create_all(eng)
