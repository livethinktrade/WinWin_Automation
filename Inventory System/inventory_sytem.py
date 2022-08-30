import pandas as pd
import datetime
import openpyxl

support_sheet = pd.read_excel('QB Item Code with CVS Price.xlsx')
cvs_price = pd.read_excel('QB Inventory.xlsx')

# selecting items that are only Active (column: Active Status) Type= Inventory Part (Column: Type)
cvs_price_filt = cvs_price[(cvs_price['Active Status'] == 'Active') & (cvs_price['Type'] == 'Inventory Part')]

cvs_price_filt = cvs_price_filt[['Item', 'Quantity On Hand']]

# adding in support sheet data
inventory = cvs_price_filt.merge(support_sheet, left_on='Item', right_on='Code', how='left')

# performing calculations for cases on hand
inventory['cases'] = round(inventory['Quantity On Hand'] / inventory['Packing - QB'])

# filtering only necessary columns
col_names = inventory.columns.to_list()
col = ['Item'] + col_names[2:7] + ['UPC', 'Code - QB', 'Item Description', 'Quantity On Hand', 'Packing - QB', 'cases']
inventory = inventory[col]

# filtering out inventory with 0 cases
inventory = inventory[inventory['cases'] != 0]

# ordering all nan value to the top
inventory = inventory.sort_values(by=['Season'])

date = datetime.datetime.today().strftime('%Y-%m-%d')

file_name = f'Inventory_{date}.xlsx'

inventory.to_excel(file_name, index=False, sheet_name='Inventory')

# Customizing tables look, feel, functionality

wb = openpyxl.load_workbook(file_name)

ws = wb['Inventory']

# adding filters
ws.auto_filter.ref = f"A1:L10000"

wb.save(file_name)
