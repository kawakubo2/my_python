import openpyxl as excel
import os
import datetime
import locale

print(f"現在のロケール: ${locale.getlocale()}")

base_dir = os.path.dirname(__file__)

book = excel.Workbook()
sheet = book.active

dt = datetime.datetime(
    year=2023, month=4, day=5, hour=15, minute=22, second=33
)

sheet.append([dt, dt, dt, dt])

sheet['A1'].number_format='yyyy/mm/dd'
sheet['B1'].number_format='yyyy年mm月dd日'
sheet['C1'].number_format='hh:mm:ss'

sheet['D1'].number_format='mm/dd HH:mm:ss'


book.save(os.path.join(base_dir, 'number_format_datetime.xlsx'))