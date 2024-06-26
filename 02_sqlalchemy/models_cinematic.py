"""
Task 3
Create a session that we will use to execute queries.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Director(Base):
    __tablename__ = "directors"

    director_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))
    surname = Column(String(30))
    rating = Column(Integer)
    movies = relationship("Movie", back_populates="director")  # Task 2

    def __repr__(self):
        return (f"<Director id={self.director_id}, "
                f"name={self.name}, "
                f"surname={self.surname}, "
                f"rating={self.rating}>")

class Movie(Base):
    __tablename__ = "movies"

    movie_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(30))
    year = Column(Integer)
    category = Column(String(20))
    director_id = Column(Integer, ForeignKey("directors.director_id"))
    rating = Column(Integer)
    director = relationship("Director", back_populates="movies")  # Task 2

    def __repr__(self):
        return (f"<Movie id={self.movie_id}, "
                f"title={self.title}, "
                f"year={self.year}, "
                f"category={self.category}, "
                f"director={self.director_id}, "
                f"rating={self.rating}>")
