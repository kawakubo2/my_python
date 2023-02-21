import cal_month
from datetime import datetime

year = int(input('年: '))
month = int(input('月: '))
day = int(input('日: '))
cal_month.print_day(cal_month.get_gessho(datetime(year, month, day)))

