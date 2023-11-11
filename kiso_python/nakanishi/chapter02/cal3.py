from calendar import TextCalendar

# 上記のようにfrom モジュール import クラスのように
# して取り込んだクラスは、使用する場合、頭にcalendar
# をつける必要がなくなる
cal = TextCalendar(6)
cal.prmonth(2023, 11)