words = ["旅行", "桜", "NG", "電信柱", "テレビ", "NG", "岸辺", "ラジオ", "NG", "ギター"]

for word in words:
    if word == "NG": continue
    print(word)

numbers = [38, 71, -10, 87, 100, 2, 48, 64, 110, 8]

total = 0
for n in numbers:
    if n < 0 or n > 100: continue
    total += n
print("合計: %d" % total)

numbers2 = [1, 2, 3, 4, 5]

for num in numbers:
    num *= 2

print(numbers2)

for i in range(len(numbers2)):
    numbers2[i] *= 2

print(numbers2)

countries = ["フランス", "アメリカ", "中国", "ドイツ", "日本"]

count = 1
for country in countries:
    print("%d: %s" % (count, country))
    count += 1

for i, country in enumerate(countries):
    print("%d: %s" % (i+1, country))

for i, _ in enumerate(numbers2):
    numbers2[i] *= 2
print(numbers2)

for num in range(len(countries)):
    print(str(num+1) + ": " + countries[num])

for index, country in enumerate(countries):
    print(str(index+1) + ": " + countries[index])

house_prices = [ 4000, 2300, 3500, 5000, 3200]
heibeis      = [ 80, 58, 72, 90, 78]
tohos        = [ 5, 20, 15, 2, 10]

for price, heibei, toho in zip(house_prices, heibeis, tohos):
    print("住宅価格:%4d 居住面積: %3d 最寄駅から徒歩: %3d分" % (price, heibei, toho))

str1 = "SMTWTFS"
str2 = "uouehra"
str3 = "nneduit"

for w1, w2, w3 in zip(str1, str2, str3):
    print(w1 + w2 + w3)

