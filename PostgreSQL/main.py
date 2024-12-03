import psycopg

try:
    # Connect to an existing database
    with psycopg.connect(
        user="postgres",
        password="1",
        host="127.0.0.1",
        port="5432",
        dbname="first_db"
    ) as connection:
        # Open a cursor to perform database operations
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM public.trends123;")
            record = cursor.fetchall()
            print(record, "\n")

except Exception as error:
    print("Error while connecting to PostgreSQL:", error)