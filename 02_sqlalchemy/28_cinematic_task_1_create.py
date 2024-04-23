"""
Task 1

Connect to the mysql server, setting the cinematic base as the home / default base. Create a table definition using SQLAlchemy:

    Directors (class) - table directors: director_id (PK), name, surname, rating
    Movies (class) - table movies: movie_id (PK), title, year, category, director_id, rating

"""

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from models_cinematic import *

CONNECTION_STRING = "mysql+pymysql://{user}:{password}@{host}/{db}"

eng = create_engine(
    CONNECTION_STRING.format(
        user="test",
        password="test",
        host="localhost",
        db="cinematic"
    )
)

Session = sessionmaker(bind=eng)

session = Session()


# Task 2: Create tables in the database.
Base.metadata.create_all(eng)

"""
Task 4

Fill in the directors and movies tables, using the session you created. 
Try with session (add / add_all). The data is on the next slide.
"""

directors = [
    {'name': 'Frank', 'surname': 'Darabont', 'rating': 7},
    {'name': 'Francis Ford', 'surname': 'Coppola', 'rating': 8},
    {'name': 'Quentin', 'surname': 'Tarantino', 'rating': 10},
    {'name': 'Christopher', 'surname': 'Nolan', 'rating': 9},
    {'name': 'David', 'surname': 'Fincher', 'rating': 7}
]

movies = [
    {'title': 'The Shawshank Redemption', 'year': 1994, 'category': 'Drama', 'director_id': 1, 'rating': 8},
    {'title': 'The Green Mile', 'year': 1999, 'category': 'Drama', 'director_id': 1, 'rating': 6},
    {'title': 'The Godfather', 'year': 1972, 'category': 'Crime', 'director_id': 2, 'rating': 7},
    {'title': 'The Godfather III', 'year': 1990, 'category': 'Crime', 'director_id': 2, 'rating': 6},
    {'title': 'Pulp Fiction', 'year': 1994, 'category': 'Crime', 'director_id': 3, 'rating': 9},
    {'title': 'Inglourious Basterds', 'year': 2009, 'category': 'War', 'director_id': 3, 'rating': 8},
    {'title': 'The Dark Knight', 'year': 2008, 'category': 'Action', 'director_id': 4, 'rating': 9},
    {'title': 'Interstellar', 'year': 2014, 'category': 'Sci-fi', 'director_id': 4, 'rating': 8},
    {'title': 'The Prestige', 'year': 2006, 'category': 'Drama', 'director_id': 4, 'rating': 10},
    {'title': 'Fight Club', 'year': 1999, 'category': 'Drama', 'director_id': 5, 'rating': 7},
    {'title': 'Zodiac', 'year': 2007, 'category': 'Crime', 'director_id': 5, 'rating': 5},
    {'title': 'Seven', 'year': 1995, 'category': 'Drama', 'director_id': 5, 'rating': 8},
    {'title': 'Alien 3', 'year': 1992, 'category': 'Horror', 'director_id': 5, 'rating': 5}
]


def insert_data(base, params):
    session.add(base(**params))
    session.commit()


for director in directors:
    insert_data(Director, director)

for movie in movies:
    insert_data(Movie, movie)