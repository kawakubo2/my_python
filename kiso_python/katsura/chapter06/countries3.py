import os, random

def create_random_list(dic):
    result = []
    for item, cnt in dic.items():
        result += [item] * cnt
    random.shuffle(result)
    return result

country_dic = {'イタリア': 13, 'イギリス': 10, 'ドイツ': 8, 'スペイン': 7, 'フランス': 4}
with open(os.path.dirname(__file__) + '/answer.txt', 'w', encoding='utf_8') as f:
    f.writelines([line + '\n' for line in create_random_list(country_dic)])
    

results = {}
with open(os.path.dirname(__file__) + '/answer.txt', 'r', encoding='utf_8') as f:
    for line in f:
        country = line.rstrip('\n')
        if country in results:
            results[country] += 1
        else:
            results[country] = 1
            
for country, count in sorted(results.items(), key=lambda c:c[1], reverse=True):
    print(f'{country}: {count}')