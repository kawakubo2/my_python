import openpyxl as excel
import os

book = excel.load_workbook(os.path.dirname(__file__) + '/uriage.xlsx')

sheet = book.create_sheet(title="4月")
sheet2 = book.copy_worksheet(book["3月"])
sheet2.title = "5月"

#book.remove(book["4月"])

book.save(os.path.dirname(__file__) + '/uriage_all4.xlsx')

