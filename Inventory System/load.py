# STEP 2 IMPORT DATA FUNCTIONS

import psycopg2
import pandas as pd
import pandas.io.sql as psql
from psycopg2 import pool
import numpy as np

from psycopg2.extensions import register_adapter, AsIs
psycopg2.extensions.register_adapter(np.int64, psycopg2._psycopg.AsIs)


class LoadData:

    def asset_valuation_insert(self, on_hand, asset_value, code, date, connection_pool):
        connection = connection_pool.getconn()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO inventory_system.asset_valuation (on_hand, asset_value, code, date) values (%s,%s,%s,%s)",
            (on_hand, asset_value, code, date))

        connection.commit()
        cursor.close()
        connection_pool.putconn(connection)

    def inventory_status_insert(self, code_qb, container_number, shipping_company, item_desc, cases,
                                case_qty, est_deliv_date, bol, status, notes, connection_pool):
        connection = connection_pool.getconn()
        cursor = connection.cursor()
        cursor.execute(
            """INSERT INTO inventory_system.asset_valuation (on_hand, asset_value, code, date) 
               values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
            (code_qb, container_number, shipping_company, item_desc, cases, case_qty, est_deliv_date, bol, status, notes))

        connection.commit()
        cursor.close()
        connection_pool.putconn(connection)





