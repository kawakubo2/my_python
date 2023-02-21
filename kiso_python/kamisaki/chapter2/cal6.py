from calendar import TextCalendar
import sys

cal = TextCalendar(6)

if len(sys.argv) != 3:
    print('使用法: python cal6.py 12 2022')
    sys.exit()

month = int(sys.argv[1])
year = int(sys.argv[1])

cal.prmonth(year, month)