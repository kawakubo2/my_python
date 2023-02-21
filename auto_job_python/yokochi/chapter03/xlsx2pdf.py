import win32com.client as com
import os

src_file = os.path.abspath(__file__)
src_dir = os.path.dirname(src_file)
in_file = os.path.join(src_dir, 'date-sample.xlsx')
pdf_file = os.path.join(src_dir, 'date-sample.pdf')

app = com.Dispatch("Excel.Application")
app.Visible = True
app.DisplayAlerts = False

book = app.Workbooks.Open(in_file)

xlTypePDF = 0
# xlTypeXPS = 1
book.ExportAsFixedFormat(xlTypePDF, pdf_file)

app.Quit()