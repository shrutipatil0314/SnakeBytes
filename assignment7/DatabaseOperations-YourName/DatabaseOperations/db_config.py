
import psycopg2

DB_USER = "postgres"
DB_PASSWORD = "your_password_here"  
DB_HOST = "localhost"
DB_PORT = "5432"

DB_NAME = "student_db"


def get_connection(dbname=DB_NAME):
    """Return a new connection to the given database (student_db by default)."""
    return psycopg2.connect(
        dbname=dbname,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
    )
