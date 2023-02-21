import datetime

d = datetime.date.today()

def youbi(year, month, day):
    if month < 3:
        year -= 1
        month += 12
    h = (year + year // 4 - year // 100 + year // 400 + (13 * month + 8) // 5 + day) % 7
    w = ['日','月','火','水','木','金','土']
    return w[h]

y = int(input('年: '))
m = int(input('月: '))
d = int(input('日: '))

print(youbi(y,m,d) + '曜日')



