import openpyxl as exel
import os

book = exel.Workbook()
sheet = book.active

for n in range(1, 10):
    c = sheet.cell(1, n)
    c.data_type = 'n'
    c.value = n

file_path = os.path.join(os.path.dirname(__file__), 'data_type.elsx')
