import random

def random_list(dic):
    result = []
    for key, count in dic.items():
        result += [key] * count
    random.shuffle(result)
    return result

answers = random_list({'イギリス': 6, 'スペイン': 8, 'ドイツ': 3, 'フランス': 9, 'イタリア': 14})
print(answers)

results = {}

for country in answers:
    if country in results:
        results[country] += 1
    else:
        results[country] = 1
        
for country, num in results.items():
    print(f"{country}: {num}")
