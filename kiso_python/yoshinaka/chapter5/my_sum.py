def my_sum(*num):
    sum = 0
    for n in num:
        sum += n
    return sum

total = my_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print('合計: {}'.format(total))

message = """
{}様
{}年{}月号が発売されました。
目次
1.aaa
2.bbb
3.ccc
"""

def create_message(message, year, month, *name):
    for n in name:
        yield message.format(n, year, month)

for m in create_message(message, 2020, 11, "山田太郎", "横山花子", "田中一郎", "山本久美子"):
    print(m)
