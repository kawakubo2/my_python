import win32com.client as com
import os

# ファイルは絶対パスで指定する必要がある
src_file = os.path.abspath(__file__)
src_dir = os.path.dirname(src_file)
in_file = src_dir+'/invoice01.xlsx'
pdf_file = src_dir+'/invoice01.pdf'

# Excelを起動
app = com.Dispatch("Excel.Application")
app.Visible = True
app.DisplayAlerts = False

# Excelでブックを読み込む
book = app.Workbooks.Open(in_file)

# ブックをPDFでエクスポート
xlTypePDF = 0 # PDFを表す定数
book.ExportAsFixedFormat(xlTypePDF, pdf_file)

# Excelを終了させる
app.Quit()