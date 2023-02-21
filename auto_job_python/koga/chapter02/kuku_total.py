import openpyxl as excel
import os

book = excel.load_workbook(os.path.dirname(__file__) + '/9x9.xlsx')
sheet = book.active

for row in sheet["A1": "I9"]:
    print(sum([cell.value for cell in row]))
