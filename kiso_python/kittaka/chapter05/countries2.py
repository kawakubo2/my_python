import random

def getRandomList(seeddic):
    result = []
    for item, cnt in seeddic.items():
        result += [item] * cnt
    random.shuffle(result)
    return result

answer = getRandomList({"イギリス": 6, "スペイン": 8, "ドイツ": 3, "フランス": 9, "イタリア": 14})

results = {}

for country in answer:
    if country in results:
        results[country] += 1
    else:
        results[country] = 1

for country, cnt in sorted(results.items(), key=lambda c: c[1], reverse=True):
    print(f"{country}: {cnt}")
        