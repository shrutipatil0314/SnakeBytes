# Task 2: Create a table in the database

import psycopg2
from db_config import get_connection


def create_table():
    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        create_sql = """
            CREATE TABLE IF NOT EXISTS students (
                student_id SERIAL PRIMARY KEY,
                name       VARCHAR(100) NOT NULL,
                age        INT,
                course     VARCHAR(50),
                marks      NUMERIC(5, 2)
            );
        """
        cur.execute(create_sql)
        conn.commit()   
        print("Table 'students' created successfully (or it already exists).")

    except psycopg2.Error as e:
        print(f"Error while creating the table: {e}")
        if conn:
            conn.rollback()
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
            print("Connection closed.")


if __name__ == "__main__":
    create_table()
