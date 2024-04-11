from mysql.connector import connect, Error

try:
    with connect(host="localhost",
                 user='test',
                 password='test',
                 database="online_movie_rating"
                 ) as conn:
        print(conn)

except Error as e:
    print(e)
