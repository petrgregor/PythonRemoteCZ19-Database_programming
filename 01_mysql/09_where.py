from mysql.connector import connect, Error

try:
    with connect(host="localhost",
                 user='test',
                 password='test',
                 database="online_movie_rating") as conn:
        with conn.cursor() as cursor:
            query = "SELECT * FROM movies WHERE id=1"
            cursor.execute(query)
            result = cursor.fetchall()
            print(f"result = {result}")
            for movie in result:
                print(*movie)

except Error as e:
    print(e)
