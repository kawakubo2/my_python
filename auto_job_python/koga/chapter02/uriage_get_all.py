import openpyxl as excel
import os

book = excel.load_workbook(os.path.dirname(__file__) + '/uriage.xlsx', data_only=True)
sheet = book.active

rows = sheet["A3":"F9"]

for row in rows:
    values = [cell.value for cell in row]
    print(values)