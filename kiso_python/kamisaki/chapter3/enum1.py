countries = ['フランス', 'アメリカ', '中国', 'ドイツ', '日本']
cnt = 0
for country in countries:
    print(str(cnt + 1) + ": " + country)
    cnt += 1

print('-------------')

for num in range(len(countries)):
    print(str(num + 1) + ": " + countries[num])

print('-------------')

for index, country in enumerate(countries):
    print(str(index + 1) + ": " + country)