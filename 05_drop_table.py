from mysql.connector import connect, Error

try:
    with connect(host="localhost",
                 user='test',
                 password='test',
                 database="online_movie_rating") as conn:
        query = """
        DROP TABLE movies
        """
        with conn.cursor() as cursor:
            cursor.execute(query)
            conn.commit()

except Error as e:
    print(e)
