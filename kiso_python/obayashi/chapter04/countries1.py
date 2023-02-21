import random_list

answer = random_list.make_random_list({'イタリア': 14, 'イギリス': 10, 'スペイン': 8, 'ドイツ': 3, 'フランス': 9})

results = {} # キーは国名, 値が得票数

for country in answer:
    if country in results:
        results[country] += 1
    else:
        results[country] = 1

for country, num in results.items():
    print(f"{country}: {num}")