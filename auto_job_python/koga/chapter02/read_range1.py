import openpyxl as excel
import os
book = excel.load_workbook(os.path.dirname(__file__) + "/test100.xlsx")
sheet = book.active

for y in range(2, 5): # 2行目から4行目を取り出す
    r = []
    for x in range(2, 5): # B列(2)からD列(4)を取り出す
        v = sheet.cell(row=y, column=x).value
        r.append(v)
    print(r)