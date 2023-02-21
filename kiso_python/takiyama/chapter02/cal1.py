import calendar

cal = calendar.TextCalendar() # TextCalendarクラスからインスタンスを生成
"""
インスタンスの中に存在する関数(メソッド)を呼び出すには変数名.メソッド名
の形で呼び出す。
"""
cal.prmonth(2022, 4)

firstweekday = cal.getfirstweekday()
print(firstweekday)
cal.setfirstweekday(6)
cal.prmonth(2022, 4)
