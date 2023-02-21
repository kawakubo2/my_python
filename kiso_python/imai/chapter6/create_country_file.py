import random

dic1 = {'イタリア': 13, 'イギリス': 10, 'ドイツ': 8, 'スペイン': 7, 'フランス': 4}

countries = [country for country, num in dic1.items() for i in range(num)]

random.shuffle(countries)

with open('answer.txt', 'w', encoding='utf_8') as f:
    f.writelines(countries)