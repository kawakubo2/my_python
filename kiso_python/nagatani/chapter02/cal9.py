import sys
from calendar import TextCalendar

if len(sys.argv) != 3:
    print('年と月を半角空白で区切って入力してください')
    print('使用例: python cal9.py 2021 8')
    sys.exit()

year = int(sys.argv[1])
month = int(sys.argv[2])

cal = TextCalendar(6)
cal.prmonth(year, month)