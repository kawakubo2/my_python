import openpyxl as excel
import os

book = excel.Workbook()
sheet = book.active

for y in range(1, 101):
    for x in range(1, 101):
        cell = sheet.cell(row=y, column=x)
        cell.value = cell.coordinate

book.save(os.path.dirname(__file__) + '/test100.xlsx')