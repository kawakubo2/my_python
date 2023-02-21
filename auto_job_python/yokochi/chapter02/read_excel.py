import openpyxl as excel
import os

book = excel.load_workbook(os.path.dirname(__file__) + '/hello.xlsx')
sheet = book.worksheets[0]
cell = sheet["A1"]
print(cell.value)