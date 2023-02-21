import os, random

def create_list(dic):
    result = []
    for item, count in dic.items():
        result += [item] * count
    random.shuffle(result)
    return result

countries = [country + "\n" for country in create_list({'イタリア': 14, 'イギリス': 13, 'ドイツ': 8, 'スペイン': 7, 'フランス': 4})]

with open(os.path.dirname(__file__) + '/countries.txt', 'w', encoding='utf_8') as f:
    f.writelines(countries)

results = {}
with open(os.path.dirname(__file__) + '/countries.txt', 'r', encoding='utf_8') as f:
    for line in f:
        country = line.rstrip("\n")
        if country in results:
            results[country] += 1
        else:
            results[country] = 1

for country, count in sorted(results.items(), key=lambda country: country[1], reverse=True):
    print(f"{country}:{count}")

