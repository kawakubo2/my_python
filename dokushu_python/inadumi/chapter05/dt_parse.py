from datetime import datetime, date, timezone, timedelta
import locale

dt1 = datetime.strptime('5.8.2019 11:37:25', '%d.%m.%Y %H:%M:%S')
print(dt1)
dt2 = datetime.fromisoformat('2019-08-05 11:37:25+09:00')
print(dt2)

dt3 = datetime.fromtimestamp(1610000000)
print(dt3)

dt4 = datetime.now()
print(dt4)
print(dt4.year)
print(dt4.month)
print(dt4.day)
print(dt4.hour)
print(dt4.minute)
print(dt4.second)
print(dt4.microsecond)
print(dt4.tzinfo)

def get_age(year, month, day):
    now = date.today()
    n_year = now.year
    age = n_year - year
    if (now.month, now.day) < (month, day):
        age -= 1
    return age

print(get_age(2000, 12, 20))

def youbi(d):
    w = '月火水木金土日'
    return w[d.weekday()]

print(youbi(dt4))

def birth_youbi(year, month, day):
    d = date(year, month, day)
    return youbi(d)

print(birth_youbi(1962, 8, 5))

dt5 = datetime(2019, 12, 4, 15, 35, 58, 469)
dt_p = dt5 + timedelta(days=15, hours=5)
dt_m = dt5 - timedelta(weeks=3)
print(dt5)
print(dt_p)
print(dt_m)

dt6 = datetime(2020, 12, 31, 23, 59, 59)
dd = dt6 - datetime.now()
print(dd)

dt7 = datetime(2021, 2, 1, 23, 59, 59)
dt8 = datetime(2020, 12, 31, 23, 59, 59)
dt9 = datetime(2021, 1, 20, 10, 33, 11)

print(dt7 == dt8)
print(dt9 < dt8)
print(dt9 > dt8)

times = [dt7, dt8, dt9]

times.sort(reverse=True)

for t in times:
    print(t)



locale.setlocale(locale.LC_ALL, 'ar_AE.UTF-8')

now = datetime.now()
print(now.strftime('%c'))
print(now.strftime('%x'))
print(now.strftime('%X'))


