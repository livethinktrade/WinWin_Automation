import os
from transform import Transform
from load import LoadData
import db_config
from Inventory_system import InventorySystem


inventory = InventorySystem()

inventory.asset_valuation_update(os.getcwd() + r'\Inventory Asset Valuation Data\2022.08.csv', date='2022.08')


