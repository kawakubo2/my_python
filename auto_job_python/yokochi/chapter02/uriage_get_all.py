# -*- coding: utf-8 -*-

import openpyxl as excel
import os

book = excel.load_workbook(os.path.dirname(__file__) + '/uriage.xlsx', data_only=True)
sheet = book.active

result = [[cell.value for cell in row] for row in sheet["A3":"F9"]]
print(result)
