import openpyxl as excel
import os

book = excel.Workbook()
sheet = book.active

for y in range(1, 10):
    for x in range(1, 10):
        cell = sheet.cell(row=y, column=x)
        cell.value = y * x

book.save(os.path.dirname(__file__) + '/9x9.xlsx')