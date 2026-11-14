# Task 3: Insert records into the table

import psycopg2
from db_config import get_connection


def insert_data():
    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        insert_sql = """
            INSERT INTO students (name, age, course, marks)
            VALUES (%s, %s, %s, %s);
        """
    
        cur.execute(insert_sql, ("Alice", 20, "Python", 85.5))
        print("Inserted 1 record: Alice")

        
        more_students = [
            ("Bob", 22, "Data Science", 78.0),
            ("Charlie", 21, "Python", 92.25),
            ("Diana", 23, "Web Development", 88.0),
            ("Ethan", 20, "Data Science", 67.5),
        ]
        cur.executemany(insert_sql, more_students)
        print(f"Inserted {len(more_students)} more records.")

        conn.commit()
        print("All records saved to the 'students' table successfully.")

    except psycopg2.Error as e:
        print(f"Error while inserting data: {e}")
        if conn:
            conn.rollback()
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
            print("Connection closed.")


if __name__ == "__main__":
    insert_data()
