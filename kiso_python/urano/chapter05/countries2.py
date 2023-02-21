# countries2.py
import random

def make_random_list(count_dic):
    result = []
    for item, count in count_dic.items():
        result += [item] * count
    random.shuffle(result)
    return result

answer = make_random_list({'イギリス': 6, 'フランス': 9, 'スペイン': 8, 'イギリス': 6, 'ドイツ': 3, 'イタリア': 14})

results = {}

for country in answer:
    if country in results:
        results[country] += 1
    else:
        results[country] = 1

for country, count in sorted(results.items(), key=lambda c: c[1], reverse=True):
    print(f"{country}: {count}")