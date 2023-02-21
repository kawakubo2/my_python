import openpyxl as excel
import os

book = excel.load_workbook(os.path.dirname(__file__) + '/test100.xlsx')
sheet = book.active

for row in sheet["B2": "D4"]:
    r = []
    for cell in row:
        r.append(cell.value)
    print(r)

for row in sheet["F3": "L25"]:
    print([cell.value for cell in row])