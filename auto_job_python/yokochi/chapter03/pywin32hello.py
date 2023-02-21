import win32com.client as com

# Excelを起動する
app = com.Dispatch("Excel.Application")
app.Visible = True
app.DisplayAlerts = False

book = app.Workbooks.Add()
sheet = book.ActiveSheet

sheet.Range("B2").Value = "こんにちは"