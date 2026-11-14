# Database Operations with PostgreSQL and Python

This is my assignment for Module 12. I used Python and the `psycopg2` library to talk to a PostgreSQL database. I made a small database called `student_db` with one table, `students`, and wrote one script for each thing the assignment asks for.

## Before you run anything

1. **Install PostgreSQL** and make sure the server is running (default port is 5432).
2. **Install psycopg2:**
   ```
   pip install psycopg2-binary
   ```
   (I used a virtual environment for this, like the module suggests: `python -m venv venv`, then activate it.)
3. **Open `db_config.py`** and change `DB_PASSWORD` to your own postgres password. Every script reads its connection details from this one file, so you only change it once.

## Files and what they do

Run them in this order, since each one builds on the last.

| File                       | What it does                                                                                           |
| -------------------------- | ------------------------------------------------------------------------------------------------------ |
| `db_config.py`             | Holds the connection settings and a `get_connection()` helper                                          |
| `task1_create_database.py` | Connects to PostgreSQL and creates the `student_db` database                                           |
| `task2_create_table.py`    | Creates the `students` table                                                                           |
| `task3_insert_data.py`     | Inserts records (one with `execute`, several with `executemany`)                                       |
| `task4_fetch_data.py`      | Fetches and prints data using `fetchone()`, `fetchall()` and `SELECT ... WHERE`                        |
| `task5_user_input.py`      | A small menu: add a student from user input and search with `WHERE`, all with parameterized queries    |
| `task6_truncate_table.py`  | Asks for confirmation, then runs `TRUNCATE TABLE`                                                      |
| `psql_commands.sql`        | The same ideas done in `psql`: create and drop a database, create a table, insert, select and truncate |
| `screenshots/`             | Screenshots of the code in VS Code and the output for each task                                        |

To run a task:

```
python task1_create_database.py
```

(use `python3` on Mac or Linux)

## The table

```
students
  student_id  SERIAL PRIMARY KEY
  name        VARCHAR(100) NOT NULL
  age         INT
  course      VARCHAR(50)
  marks       NUMERIC(5,2)
```

## Things I paid attention to

- **Parameterized queries.** Anywhere a value comes from the user (or even from a variable), I used `%s` placeholders and passed the values separately, like `cur.execute(sql, (name, age))`. I did not put values into the SQL with f-strings, because that opens the door to SQL injection.
- **`conn.commit()`.** Anything that changes data (CREATE TABLE, INSERT, TRUNCATE) only gets saved after a commit. I also call `rollback()` if something goes wrong.
- **Closing connections.** Each script closes its cursor and connection in a `finally` block so nothing stays open if there's an error.
- **Creating the database.** `CREATE DATABASE` can't run inside a transaction, so in Task 1 I turned on `autocommit`. I also connect to the default `postgres` database first, since `student_db` doesn't exist yet.
- **Safe to re-run.** Task 1 checks whether the database exists, and Task 2 uses `CREATE TABLE IF NOT EXISTS`. Task 6 asks "yes/no" before deleting anything, because TRUNCATE can't be undone.

## What you should see

- Task 1: a message that the database was created
- Task 2: a message that the table was created
- Task 3: a message for every record inserted
- Task 4: the records printed in the terminal, including the filtered ones
- Task 5: a menu where you can add and search students
- Task 6: the row count before and after the truncate (the second one is 0)

## Problems I ran into

- If you get `password authentication failed`, the password in `db_config.py` is wrong.
- If you get `could not connect to server`, PostgreSQL isn't running or the port is different.
- If Task 3 is run twice you'll get duplicate students. That's fine, since the table has no unique constraint on the name. Run Task 6 to clear it.
