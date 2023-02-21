import random, os

def getRandomList(seeddic):
    result = []
    for item, cnt in seeddic.items():
        result += [item] * cnt
    random.shuffle(result)
    return result

answer = getRandomList({"イギリス": 6, "スペイン": 8, "ドイツ": 3, "フランス": 9, "イタリア": 14})

outputpath = os.path.join(os.path.dirname(__file__), 'answer.txt')
with open(outputpath, "w", encoding="utf_8") as inputf:
    inputf.writelines([country + "\n" for country in answer])

results = {}
inputpath = os.path.join(os.path.dirname(__file__), 'answer.txt')
with open(inputpath, "r", encoding="utf_8") as f:
    for country in f:
        country = country.rstrip("\n")
        if country in results:
            results[country] += 1
        else:
            results[country] = 1

for country, cnt in sorted(results.items(), key=lambda c: c[1], reverse=True):
    print(f"{country}: {cnt}")
        