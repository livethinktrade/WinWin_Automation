import os
from transform import Transform
from load import LoadData
import db_config
import pandas as pd


class InventorySystem:

    def __init__(self):

        self.support_sheet = pd.read_excel(os.getcwd() + r'\QB Item COde with CVS Price.xlsx')
        self.transform = Transform()
        self.load = LoadData()

    def asset_valuation_update(self, file, date):

        asset_valuation_table = self.transform.inventory_asset_valuation(
            file=file,
            date=date)
        i = 0

        with db_config.PsycoPoolDB() as connection_pool:
            while i < len(asset_valuation_table):
                on_hand = asset_valuation_table.loc[i, 'On Hand']
                asset_value = asset_valuation_table.loc[i, 'Asset Value']
                code = asset_valuation_table.loc[i, 'Code']
                date = asset_valuation_table.loc[i, 'date']

                self.load.asset_valuation_insert(on_hand, asset_value, code, date, connection_pool)

                i += 1

    def shipping_status(self, file):

        items_shipped = pd.read_excel(file)

        i = 0

        with db_config.PsycoPoolDB() as connection_pool:
            while i < len(items_shipped):

                code_qb = items_shipped.loc[i, ]
                container_number = items_shipped.loc[i, ]
                shipping_company = items_shipped.loc[i, ]
                item_desc = items_shipped.loc[i, ]
                cases = items_shipped.loc[i, ]
                case_qty = items_shipped.loc[i, ]
                est_deliv_date = items_shipped.loc[i, ]
                bol = items_shipped.loc[i, ]
                shipping_status = items_shipped.loc[i, ]
                notes = items_shipped.loc[i, ]

                self.load.inventory_status_insert(code_qb, container_number, shipping_company, item_desc, cases,
                                                  case_qty, est_deliv_date, bol, shipping_status, notes, connection_pool)
                i += 1

