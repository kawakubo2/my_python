# -*- coding: utf-8 -*-

import openpyxl as excel
import os

book = excel.load_workbook(os.path.dirname(__file__) + '/test100.xlsx')
sheet = book.active

result2 = [[cell.value for cell in row] for row in sheet["B2":"D4"]]
print(result2)

