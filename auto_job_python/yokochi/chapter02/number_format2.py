import openpyxl as excel
import os

base_dir = os.path.dirname(__file__)

book = excel.Workbook()
sheet = book.active

val = 3.5123
sheet.append([val, val, val])

sheet['A1'].number_format = '0'
sheet['B1'].number_format = '0.00'
sheet['C1'].number_format = '0.0000'

def set_cell(cname, value, fmt):
    c = sheet[cname]
    c.value = value
    c.number_format = fmt

val2 = 275209398
val3 = -275209398
num_fmt = '#,##0:[red]""#,##0'
set_cell("A2", val2, num_fmt)
set_cell("B2", val3, num_fmt)

book.save(os.path.join(base_dir, 'number_format.xlsx'))
