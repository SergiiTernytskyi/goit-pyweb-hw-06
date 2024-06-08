import psycopg2
from contextlib import contextmanager


@contextmanager
def create_connection():
    """create a database connection to a Postgres database"""

    try:
        connection = psycopg2.connect(
            host="localhost", database="homework", user="postgres", password="postgres"
        )
        yield connection
        connection.close()
    except psycopg2.OperationalError as error:
        raise RuntimeError(f"Failed to create connection {error}")
