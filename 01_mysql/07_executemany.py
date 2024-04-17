from mysql.connector import connect, Error

try:
    with connect(host="localhost",
                 user='test',
                 password='test',
                 database="online_movie_rating") as conn:
        query = """
        INSERT INTO movies (title)
        VALUES ( %s )
        """
        movies = [("Kameňák 2",), ("Kmotr",), ("Kmotr 2",)]
        with conn.cursor() as cursor:
            cursor.executemany(query, movies)
            conn.commit()

except Error as e:
    print(e)
