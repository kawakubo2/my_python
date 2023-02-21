from datetime import datetime, date, timedelta, timezone, time

print(datetime.today())
print(date.today())
print(datetime.now())
print(datetime.now(timezone(timedelta(hours=9))))
print(datetime.utcnow())
print(datetime.now(timezone.utc))

print(date(1962, 8, 5))
print(time(19, 57, 30))