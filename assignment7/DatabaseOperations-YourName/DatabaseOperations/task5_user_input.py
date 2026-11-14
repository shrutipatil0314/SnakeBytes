# Task 5: Take input from the user and insert it with a parameterized query,

import psycopg2
from db_config import get_connection


def add_student():
    name = input("Enter student name: ").strip()
    if not name:
        print("Name can't be empty.")
        return

    try:
        age = int(input("Enter age: "))
        marks = float(input("Enter marks: "))
    except ValueError:
        print("Age and marks must be numbers. Nothing was added.")
        return

    course = input("Enter course: ").strip()

    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO students (name, age, course, marks) VALUES (%s, %s, %s, %s);",
            (name, age, course, marks),
        )
        conn.commit()
        print(f"Student '{name}' added successfully!")
    except psycopg2.Error as e:
        print(f"Error while adding the student: {e}")
        if conn:
            conn.rollback()
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def search_by_course():
    course = input("Enter a course to search for: ").strip()

    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "SELECT student_id, name, age, course, marks FROM students WHERE course = %s;",
            (course,),
        )
        rows = cur.fetchall()
        if rows:
            print(f"\n--- Students in '{course}' ---")
            for row in rows:
                print(f"ID: {row[0]} | Name: {row[1]} | Age: {row[2]} | "
                      f"Course: {row[3]} | Marks: {row[4]}")
        else:
            print(f"No students found in the course '{course}'.")
    except psycopg2.Error as e:
        print(f"Error while searching: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def search_by_min_marks():
    try:
        min_marks = float(input("Show students with marks above: "))
    except ValueError:
        print("Please enter a number.")
        return

    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "SELECT student_id, name, course, marks FROM students "
            "WHERE marks > %s ORDER BY marks DESC;",
            (min_marks,),
        )
        rows = cur.fetchall()
        if rows:
            print(f"\n--- Students with marks above {min_marks} ---")
            for row in rows:
                print(f"ID: {row[0]} | Name: {row[1]} | Course: {row[2]} | Marks: {row[3]}")
        else:
            print(f"Nobody has marks above {min_marks}.")
    except psycopg2.Error as e:
        print(f"Error while searching: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def main():
    while True:
        print("\n--- Student Database ---")
        print("1. Add a student")
        print("2. Search students by course")
        print("3. Search students by minimum marks")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            search_by_course()
        elif choice == "3":
            search_by_min_marks()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
