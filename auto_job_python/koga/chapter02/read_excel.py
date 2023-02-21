import openpyxl as excel
import os

book = excel.load_workbook(os.path.dirname(__file__) + "/クロスエイジ様9月分請求書.xlsx")

sheet = book.worksheets[0]

cell = sheet['I20']

print(cell.value)