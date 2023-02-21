for i in range(10):
    print(i)

numbers = [1, 2, 4, 8, 16, 32, 64]

for n in numbers:
    print(n)

str1 = "abcdefghi"

for c in str1:
    print(c)

str2 = "日月火水木金土"

for s in str2:
    print(s + "曜日")

weekdays = {"日": "Sun", "月": "Mon", "火": "Tue", "水": "Wed","木": "Thu", "金": "Fri", "土": "Sat"}

for ja, en in weekdays.items():
    print(ja, en)

it = iter(str2)
while True:
    try:
        print(next(it))
    except StopIteration:
        break

# 糖衣構文(Syntax Sugar)
        pass
for c in str2:
    print(c)

n = 0.0
while n <= 1.0:
    n += 0.01
    print(n)

for n in range(1, 101):
    print("{:.2f}".format(n / 100))

words = ["旅行", "桜", "テレビ", "終了", "岸辺", "ラジオ"]

for word in words:
    if word == "終了":
        print("*ループを中断しました")
        break
    print(word)