import logging
from psycopg2 import DatabaseError

from connect import create_connection


def create_table(connection, sql_expression):
    c = connection.cursor()

    try:
        c.execute(sql_expression)
        connection.commit()
    except DatabaseError as error:
        logging.error(error)
        connection.rollback()
    finally:
        c.close()


if __name__ == "__main__":
    sql_create_groups_table = """
    DROP TABLE IF EXISTS groups;
    CREATE TABLE groups (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL
    );
    """

    sql_create_students_table = """
    DROP TABLE IF EXISTS students;
    CREATE TABLE students (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(150) NOT NULL,
        last_name VARCHAR(150) NOT NULL,
        group_id INTEGER REFERENCES groups(id)
            ON DELETE CASCADE    
    );
    """

    sql_create_teachers_table = """
    DROP TABLE IF EXISTS teachers;
    CREATE TABLE teachers (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(150) NOT NULL,
        last_name VARCHAR(150) NOT NULL
    );
    """

    sql_create_subjects_table = """
    DROP TABLE IF EXISTS subjects;
    CREATE TABLE subjects (
        id SERIAL PRIMARY KEY,
        name VARCHAR(150) NOT NULL,
        teacher_id INTEGER REFERENCES teachers(id)
            ON DELETE CASCADE 
    );
    """

    sql_create_marks_table = """
    DROP TABLE IF EXISTS marks;
    CREATE TABLE marks (
        id SERIAL PRIMARY KEY,
        student_id INTEGER REFERENCES students(id)
            ON DELETE CASCADE,
        subject_id INTEGER REFERENCES subjects(id)
            ON DELETE CASCADE,
        mark INTEGER CHECK (mark >= 0 AND mark <= 100),
        mark_date DATE NOT NULL
    );
    """

    try:
        with create_connection() as connection:
            if connection is not None:
                # Create groups table
                create_table(connection, sql_create_groups_table)

                # Create students table
                create_table(connection, sql_create_students_table)

                # Create teachers table
                create_table(connection, sql_create_teachers_table)

                # Create subjects table
                create_table(connection, sql_create_subjects_table)

                # Create marks table
                create_table(connection, sql_create_marks_table)
            else:
                print("Error! cannot create the database connection.")
    except RuntimeError as error:
        logging.error(error)
