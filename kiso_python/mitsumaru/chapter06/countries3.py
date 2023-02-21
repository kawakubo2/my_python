import os

results = {}

with open(os.path.dirname(__file__) + '/answer.txt', 'r', encoding='utf_8') as f:
    for line in f:
        country = line.rstrip('\n')
        if country in results:
            results[country] += 1
        else:
            results[country] = 1

for country, num in sorted(results.items(), key=lambda r: r[1], reverse=True):
    print(f"{country}: {num}")

