import pandas as pd
import os


class Transform:

    def __init__(self, support_sheet=None):

        self.support_sheet = pd.read_excel(f"{support_sheet}")

    def inventory_asset_valuation(self, file):

        inventory_val = pd.read_csv(file)

        inventory_val = inventory_val.rename(columns={'Unnamed: 0': 'Code'})

        inventory_val = inventory_val[['On Hand', 'Asset Value', 'Code']]

        inventory_val[['Code', 'trash']] = inventory_val.Code.str.split(' ', expand=True, n=1)

        inventory_val = inventory_val[['On Hand', 'Asset Value', 'Code']]

        # drop nan values & last 2 rows

        inventory_val = inventory_val[:-2]
        inventory_val = inventory_val.dropna()

        # filter all items that have a 0 on hand and 0 value
        inventory_val = inventory_val[(inventory_val['On Hand'] != 0) & (inventory_val['Asset Value'] != 0)]

        # support_sheet = self.support_sheet.copy()
        #
        # support_sheet = support_sheet[['Code', 'Item Description', 'Season', 'Type', 'Display', 'URC']]
        #
        # inventory_val = inventory_val.merge(support_sheet, left_on='Code', right_on='Code', how='left')

        return inventory_val


a = Transform('QB Item COde with CVS Price.xlsx')

test = a.inventory_asset_valuation(r'C:\Users\User1\OneDrive\WinWin Staff Folders\Michael\Automation\Inventory System\Inventory Asset Valuation Data\2021.01.csv')

test.to_excel('sample.xlsx', index=False)