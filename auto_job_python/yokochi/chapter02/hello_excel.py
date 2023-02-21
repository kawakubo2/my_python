import openpyxl as excel
import os

book = excel.Workbook()
sheet = book.active
sheet["A1"] = "こんにちは"

book.save(os.path.dirname(__file__) + './hello.xlsx')