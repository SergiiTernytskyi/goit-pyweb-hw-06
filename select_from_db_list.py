import logging
import os

from psycopg2 import DatabaseError

from connect import create_connection


if __name__ == "__main__":
    try:
        with create_connection() as connection:
            if connection is not None:
                c = connection.cursor()

                sql_files = [file for file in os.listdir() if file.endswith(".sql")]

                try:
                    for file_path in sql_files:
                        with open(file_path, "r", encoding="utf-8") as file:
                            sql_query = file.read()

                        print("===" * 50)
                        c.execute(sql_query)
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
