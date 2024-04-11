"""
Task 3

Write an SQL query that will create the following tables in the cinematic database:

    directors: director_id(PK), name, surname, rating
    movies: movie_id(PK), title, year, category, director_id(FK), rating
"""

from mysql.connector import connect, Error

try:
    with connect(host="localhost",
                 user='test',
                 password='test',
                 database="cinematic"
                 ) as conn:
        query = ""  # TODO: doplnit kód
        with conn.cursor() as cursor:
            cursor.execute(query)
            conn.commit()

except Error as e:
    print(e)
