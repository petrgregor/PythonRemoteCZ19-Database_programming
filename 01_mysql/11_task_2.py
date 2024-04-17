from mysql.connector import connect, Error

try:
    with connect(host="localhost",
                 user='test',
                 password='test',
                 database="cinematic"
                 ) as conn:
        print(conn)

except Error as e:
    print(e)
