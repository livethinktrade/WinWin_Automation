# STEP 2 IMPORT DATA FUNCTIONS

import psycopg2
import pandas as pd
import pandas.io.sql as psql
from psycopg2 import pool
import numpy as np

from psycopg2.extensions import register_adapter, AsIs
psycopg2.extensions.register_adapter(np.int64, psycopg2._psycopg.AsIs)


def asset_valuation_insert(on_hand, asset_valuation, code, date, connection_pool):
    connection = connection_pool.getconn()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO inventory_system.asset_valuation (on_hand, asset_valuation, code, date) values (%s,%s,%s,%s)",
        (on_hand, asset_valuation, code, date))

    connection.commit()
    cursor.close()
    connection_pool.putconn(connection)


# def size_table_update(code, size, connection_pool):
#     connection = connection_pool.getconn()
#     cursor = connection.cursor()
#     cursor.execute(
#         f"update item_size set size = '{size}' where code = '{code}'")
#
#     connection.commit()
#     cursor.close()
#     connection_pool.putconn(connection)