from sqlalchemy import create_engine, MetaData, select, desc, and_, or_
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

conn = eng.connect()

"""
Task 5
List all movies from the Drama category. Use select () and query ().
"""
print("========= TASK 5 ==========")
print("List all movies from the Drama category. Use select().")
query = select([Movie]).where(Movie.category == "Drama")
#print(query)
query_result = conn.execute(query).fetchall()
for movie in query_result:
    print(movie)

print("List all movies from the Drama category. Use query().")
query_result = session.query(Movie).filter_by(category="Drama")
for result in query_result:
    print(result)

"""
Task 6
List the titles of movies from the Crime category that were produced after 1994. 
Use select () and query ().
"""
print("========= TASK 6 ==========")
print("List the titles of movies from the Crime category that were produced after 1994. "
      "Use select()")
query = select([Movie]).where(Movie.category == "Crime", Movie.year >= 1994)
print(query)
query_result = conn.execute(query).fetchall()
for movie in query_result:
    print(movie)

print("List the titles of movies from the Crime category that were produced after 1994. "
      "Use query()")
query_result = session.query(Movie).filter(Movie.category == "Crime", Movie.year >= 1994).order_by()
print(query_result.statement)
for movie in query_result:
    print(movie)

"""
Task 7

List the categories of all films and their ranking for films 
that were produced in the years 2000-2010 
and whose ranking is greater than 7, sorting by ranking. Use query().
"""
print("========= TASK 7 ==========")
query_result = (session.query(Movie.category, Movie.rating)
                .filter(Movie.year >= 2000, Movie.year <= 2010, Movie.rating > 7)
                .order_by(desc(Movie.rating)))
for result in query_result:
    category, rating = result
    print(f"{category}: {rating}")

"""
Task 8

List the names of all directors whose ranking is greater than or equal to 6 
and whose first name starts with the letter 'D' or ends with the letter 'n'. Use query ().
"""
print("========= TASK 8 ==========")
query_result = (session.query(Director)
                .filter(and_(Director.rating >= 6, or_(Director.name.startswith("D"), Director.name.endswith("n")))))
for result in query_result:
    print(result)

print("========= Using join ==========")
"""
Task 1

List the names and surnames of all directors whose films were made between 2011 and 2014, 
and the rating of their films is less than 9. Use query().
"""
print("========= Task 1 ==========")
query_result = session.query(Director.name, Director.surname).join(Movie).filter(Movie.year >= 2011, Movie.year <= 2014, Movie.rating < 9)
for result in query_result:
    print(result)