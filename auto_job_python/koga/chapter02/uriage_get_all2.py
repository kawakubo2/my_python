import openpyxl as excel
import os

book = excel.load_workbook(os.path.dirname(__file__) + '/uriage.xlsx')
sheet = book.active

rows = sheet["A3": "F9"]
print("内包表記を使う方法")
for row in rows:
    values = [cell.value for cell in row]
    print(values)

print("内包表記を使わない方法")
for row in rows:
    values = []
    for cell in row:
        values.append(cell.value)
    print(values)