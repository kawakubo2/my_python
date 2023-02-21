# -*- coding: utf-8 -*-

countries = ['フランス', 'アメリカ', '中国', 'ドイツ', '日本']

print('===< 番号を振りたい >===')
print('---< 方法1 >---')
cnt = 0
for country in countries:
    print(str(cnt + 1) + ': ' + country)
    cnt += 1
    
print('---< 方法2 >---')
for num in range(len(countries)):
    print(str(num + 1) + ': ' + countries[num])
    
print('---< 方法3 >---')
for index, country in enumerate(countries):
    print(str(index + 1) + ': ' + country)
    
