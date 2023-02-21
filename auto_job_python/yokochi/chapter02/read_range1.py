# -*- coding: utf-8 -*-

import openpyxl as excel
import os

book = excel.load_workbook(os.path.dirname(__file__) + '/test100.xlsx')
sheet = book.active

result = []
for row_num in range(2, 5):
    r = []
    for column_num in range(2, 5):
        r.append(sheet.cell(row=row_num, column=column_num).value)
    result.append(r)
    
print(result)
