import logging

from psycopg2 import DatabaseError

from connect import create_connection

if __name__ == "__main__":
    query_01 = """
    SELECT s.id,
        s.first_name,
        s.last_name,
        AVG(m.mark) as average_mark
    FROM students as s
    JOIN marks as m ON s.id = m.student_id  
    GROUP BY s.id
    ORDER BY average_mark ASC
    LIMIT 5;
    """

    try:
        with create_connection() as connection:
            if connection is not None:
                c = connection.cursor()
                try:
                    c.execute(query_01)
                    result = c.fetchall()
                    print(result)
                except DatabaseError as error:
                    logging.error(error)
                finally:
                    c.close()
            else:
                print("Error! cannot create the database connection.")
    except RuntimeError as err:
        logging.error(err)
