# Task 1: Connect to PostgreSQL and create a database


import psycopg2
from db_config import get_connection, DB_NAME


def create_database():
    conn = None
    cur = None
    try:
        conn = get_connection("postgres")
        conn.autocommit = True
        cur = conn.cursor()
        print("Connected to PostgreSQL successfully.")

     
        cur.execute("SELECT 1 FROM pg_database WHERE datname = %s;", (DB_NAME,))
        if cur.fetchone():
            print(f"Database '{DB_NAME}' already exists, nothing to do.")
        else:
         
            cur.execute(f"CREATE DATABASE {DB_NAME};")
            print(f"Database '{DB_NAME}' created successfully.")

    except psycopg2.Error as e:
        print(f"Error while creating the database: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
            print("Connection closed.")


if __name__ == "__main__":
    create_database()
