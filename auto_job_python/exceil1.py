import openpyxl as excel
import os

book = excel.Workbook()
sheet = book.active
for i in range(1, 10):
    for j in range(1, 10):
        sheet.cell(row=i, column=j, value=i * j)

book.save(os.path.dirname(__file__) + '/kuku.xlsx')