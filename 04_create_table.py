from mysql.connector import connect, Error

try:
    with connect(host="localhost",
                 user='test',
                 password='test',
                 database="online_movie_rating") as conn:
        query = """
        CREATE TABLE movies(
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(100)
        )
        """
        with conn.cursor() as cursor:
            cursor.execute(query)
            conn.commit()

except Error as e:
    print(e)
