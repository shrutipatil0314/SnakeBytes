# Task 4: Fetch and display data from the table
# Uses fetchone(), fetchall() and SELECT with WHERE conditions.

import psycopg2
from db_config import get_connection


def print_student(row):
    print(f"ID: {row[0]} | Name: {row[1]} | Age: {row[2]} | "
          f"Course: {row[3]} | Marks: {row[4]}")


def fetch_data():
    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()

       
        cur.execute("SELECT * FROM students ORDER BY student_id;")
        first = cur.fetchone()
        print("--- First record (fetchone) ---")
        if first:
            print_student(first)
        else:
            print("The table is empty. Run task3_insert_data.py first.")

       
        cur.execute("SELECT * FROM students ORDER BY student_id;")
        rows = cur.fetchall()
        print(f"\n--- All records (fetchall) - {len(rows)} found ---")
        for row in rows:
            print_student(row)

        cur.execute("SELECT * FROM students WHERE marks > %s ORDER BY marks DESC;", (80,))
        top = cur.fetchall()
        print("\n--- Students with marks above 80 ---")
        for row in top:
            print_student(row)

        cur.execute("SELECT * FROM students WHERE course = %s;", ("Python",))
        python_students = cur.fetchall()
        print("\n--- Students in the Python course ---")
        for row in python_students:
            print_student(row)

        print("\nData fetched successfully.")

    except psycopg2.Error as e:
        print(f"Error while fetching data: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
            print("Connection closed.")


if __name__ == "__main__":
    fetch_data()
