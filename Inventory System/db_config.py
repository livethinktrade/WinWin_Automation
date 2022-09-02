import psycopg2
from psycopg2 import pool
import sqlalchemy
import pandas.io.sql as psql


localAddress = 'localhost'
database = 'test'
username = 'postgres'  # add your database username
password_parameter = 'winwin'  # add your database password
port_parameter = 5432


def create_pool_dbconnection():
    connection_pool = None
    try:

        connection_pool = pool.SimpleConnectionPool(1, 10000,
                                                    database=database,
                                                    user=username,
                                                    password=password_parameter,
                                                    host=localAddress,
                                                    port=port_parameter)

        return connection_pool

    except Exception as error:
        print(error)
        if connection_pool is not None:
            connection_pool.closeall()


def engine_pool_connection():

    """creates a database connection. returns an engine class from sqlalchemy"""
    try:

        engine = sqlalchemy.create_engine(
            f"postgresql://{username}:{password_parameter}@{localAddress}:{port_parameter}/{database}",
            pool_size=50, max_overflow=0)
        return engine

    except Exception as error:
        print(error)


class EnginePoolDB:

    def __init__(self):
        try:

            self.engine = sqlalchemy.create_engine(
                f"postgresql://{username}:{password_parameter}@{localAddress}:{port_parameter}/{database}",
                pool_size=50, max_overflow=0)

        except Exception as error:
            print(error)

    def __enter__(self):
        return self.engine

    def __exit__(self, *args, **kwargs):
        self.engine.dispose()
