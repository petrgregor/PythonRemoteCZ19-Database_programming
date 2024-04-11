from mysql.connector import connect, Error

try:
    with connect(host="localhost",
                 user='test',
                 password='test',
                 database="online_movie_rating") as conn:
        cursor = conn.cursor()
        query = "SELECT * FROM movies"
        cursor.execute(query)
        print(f"cursor = {cursor}")
        result = cursor.fetchall()
        print(f"result = {result}")
        for movie in result:
            print(*movie)

        print("=====================")
        with conn.cursor() as cursor:
            query = "SELECT title FROM movies"
            cursor.execute(query)
            print(f"cursor = {cursor}")
            result = cursor.fetchall()
            print(f"result = {result}")
            for movie in result:
                print(*movie)

except Error as e:
    print(e)
