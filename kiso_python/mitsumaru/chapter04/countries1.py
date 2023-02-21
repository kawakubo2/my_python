import random

country_map = {'イギリス': 6, 'スペイン': 8, 'ドイツ': 3, 'フランス': 9, 'イタリア': 14}
countries = []
for country, num in country_map.items():
    countries += [country] * num

random.shuffle(countries)

print(countries)

results = {}

for country in countries:
    if country in results:
        results[country] += 1 # results = results + 1
    else:
        results[country] = 1

for country, num in results.items():
    print(f'{country}: {num}')