import openpyxl as excel
import os

book = excel.Workbook()

sheet = book.active

for i in range(1, 11):
    sheet.cell(row=i, column=1, value=i)

book.save(os.path.dirname(__file__) + '/renzoku.xlsx')