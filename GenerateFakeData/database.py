import psycopg2


def create_connect():
    conn = psycopg2.connect(
        database="postgres",
        host="localhost",
        user="postgres",
        password="Manager1",
        port=5432
    )
    return conn
