# -*- coding: utf-8 -*-

import openpyxl as excel
import os

sheet = excel.load_workbook(os.path.dirname(__file__) + '/uriage.xlsx', data_only=True).active

for row in sheet.iter_rows(min_row=3):
    values = [cell.value for cell in row]
    if values[0] is None: break
    print(values)