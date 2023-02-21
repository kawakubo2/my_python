import openpyxl as excel
import os

book = excel.load_workbook(os.path.dirname(__file__) + '/uriage.xlsx', data_only=True)
sheet = book.active

for row in sheet["A3": "F999"]:
    values = [cell.value for cell in row]
    if values[0] is None: break
    print(values)
