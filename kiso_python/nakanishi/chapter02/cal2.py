import calendar

# calendarモジュールの中で定義されているTextCalendarコンストラクタ
# を使用して、calendarインスタンスを生成している。
cal = calendar.TextCalendar(6)
cal.prmonth(2023, 11)