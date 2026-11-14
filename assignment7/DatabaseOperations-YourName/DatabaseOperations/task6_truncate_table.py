# Task 6: TRUNCATE the table

import psycopg2
from db_config import get_connection


def count_rows(cur):
    cur.execute("SELECT COUNT(*) FROM students;")
    return cur.fetchone()[0]


def truncate_table():
    answer = input("This will delete ALL rows from 'students'. Continue? (yes/no): ")
    if answer.strip().lower() != "yes":
        print("Cancelled. Nothing was deleted.")
        return

    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        print(f"Rows before truncate: {count_rows(cur)}")

   
        cur.execute("TRUNCATE TABLE students RESTART IDENTITY;")
        conn.commit()
        print("Table 'students' truncated successfully.")

        print(f"Rows after truncate: {count_rows(cur)}")

    except psycopg2.Error as e:
        print(f"Error while truncating the table: {e}")
        if conn:
            conn.rollback()
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
            print("Connection closed.")


if __name__ == "__main__":
    truncate_table()
