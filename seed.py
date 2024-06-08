import logging
from random import randint

from faker import Faker
from psycopg2 import DatabaseError

from connect import create_connection


fake = Faker("uk-Ua")

STUDENTS_COUNT = 50
GROUPS_COUNT = 3
SUBJECTS_COUNT = 5
TEACHERS_COUNT = 5
MARKS_COUNT = 20


def insert_data(connection):
    c = connection.cursor()

    for _ in range(GROUPS_COUNT):
        c.execute(
            "INSERT INTO groups (name) VALUES (%s)",
            (fake.words(nb=2),),
        )

    for _ in range(TEACHERS_COUNT):
        c.execute(
            "INSERT INTO teachers (first_name, last_name) VALUES (%s, %s)",
            (fake.first_name(), fake.last_name()),
        )

    for _ in range(SUBJECTS_COUNT):
        for teacher_id in range(1, TEACHERS_COUNT + 1):
            c.execute(
                "INSERT INTO subjects (name, teacher_id) VALUES (%s, %s)",
                (fake.words(nb=3), teacher_id),
            )

    for group_id in range(1, GROUPS_COUNT + 1):
        for _ in range(STUDENTS_COUNT):
            c.execute(
                "INSERT INTO students (first_name, last_name, group_id) VALUES (%s, %s, %s) RETURNING id",
                (fake.first_name(), fake.last_name(), group_id),
            )

            student_id = c.fetchone()[0]

            for subject_id in range(1, SUBJECTS_COUNT + 1):
                for _ in range(MARKS_COUNT):
                    c.execute(
                        "INSERT INTO marks (student_id, subject_id, mark, mark_date) VALUES (%s, %s, %s, %s)",
                        (
                            student_id,
                            subject_id,
                            randint(0, 100),
                            fake.date_this_year(),
                        ),
                    )

    try:
        connection.commit()
    except DatabaseError as e:
        logging.error(e)
        connection.rollback()
    finally:
        c.close()


if __name__ == "__main__":
    try:
        with create_connection() as connection:
            if connection is not None:
                insert_data(connection)
            else:
                logging.error("Error! cannot create the database connection.")
    except RuntimeError as err:
        logging.error(err)
