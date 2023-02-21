numbers = [1, 2, 3, 4, 5, 6, 7]

for num in numbers:
    print(num)

s = "上崎玲"

for c in s:
    print(c + "の文字コード" + str(ord(c)))

s2 = "日月火水木金土"

for w in s2:
    print(w + "曜日")

flowers = ['Rose', 'Tulip', 'Morning Glory', 'Sun flower']
# 糖衣構文(シンタックスシュガー)
for flower in flowers:
    print(flower)

"""
itr = iter(flowers)
while True:
    try:
        print(next(itr))
    except StopIteration:
        pass
"""