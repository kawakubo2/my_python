from make_random_list import make_random_list

answer = make_random_list({'イギリス': 6, 'スペイン': 8, 'ドイツ': 3,
                           'フランス': 9, 'イタリア': 14})

results = {}

for country in answer:
    if country in results:
        results[country] += 1
    else:
        results[country] = 1

for country, num in results.items():
    print(f"{country}: {num}")