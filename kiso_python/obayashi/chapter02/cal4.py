from calendar import TextCalendar

year = int(input('年を入力してください: '))
month = int(input('月を入力してください: '))

cal = TextCalendar(6)
cal.prmonth(year, month)

age = 18

if age >= 20:
    print('お酒の販売は可能です')

else:
    print('お酒の販売は出来ません。')