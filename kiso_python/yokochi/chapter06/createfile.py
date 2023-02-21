# createfile.py
import random, os

def make_shuffle_list(dic):  # {'イタリア': 14, 'イギリス': 10, ...}
    result = []
    for country, cnt in dic.items():
        result += [country] * cnt
    random.shuffle(result)
    return result

result = make_shuffle_list({'イタリア': 13, 'イギリス': 10, 'ドイツ': 5, 'スペイン': 7, 'フランス': 4})

with open(os.path.dirname(__file__) + '/answer.txt', 'w', encoding='utf_8') as f:
    f.writelines([line + "\n" for line in result])