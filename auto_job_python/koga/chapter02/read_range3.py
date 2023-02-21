import openpyxl as excel
import os

def read_range(sheet, min_row, max_row, min_col, max_col):
    result = []
    it = sheet.iter_rows(min_row, max_row, min_col, max_col)
    for row in it:
        line = []
        for cell in row:
            line.append(cell.value)
        result.append(line)
    return result

book = excel.load_workbook(os.path.dirname(__file__) + "/test100.xlsx")
sheet = book.active

array2d = read_range(sheet, 2, 4, 1, 5)
print(array2d)