CREATE DATABASE student_db;      
CREATE DATABASE test_db;         
\l                               

DROP DATABASE test_db;          
\l                             


\c student_db                   

CREATE TABLE IF NOT EXISTS students (
    student_id SERIAL PRIMARY KEY,
    name       VARCHAR(100) NOT NULL,
    age        INT,
    course     VARCHAR(50),
    marks      NUMERIC(5, 2)
);

\dt                             
\d students                     

INSERT INTO students (name, age, course, marks) VALUES ('Alice', 20, 'Python', 85.5);
INSERT INTO students (name, age, course, marks) VALUES ('Bob', 22, 'Data Science', 78.0);
INSERT INTO students (name, age, course, marks) VALUES ('Charlie', 21, 'Python', 92.25);


SELECT * FROM students;
SELECT * FROM students WHERE marks > 80;
SELECT name, marks FROM students WHERE course = 'Python';


TRUNCATE TABLE students RESTART IDENTITY;
SELECT * FROM students;         

\q
