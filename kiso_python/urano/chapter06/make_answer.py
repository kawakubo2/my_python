# make_answer.py
import random, os

def make_shuffle_list(dic):
    result = []
    for item, cnt in dic.items():
        result += [item] * cnt
    random.shuffle(result)
    return result

answer = make_shuffle_list({'イタリア': 14, 'イギリス': 10, 
                        'ドイツ': 8, 'スペイン': 7, 'フランス': 4})
print(answer)

with open(os.path.dirname(__file__) + '/answer.txt', 'w', encoding='utf_8') as f:
    f.writelines([line + '\n' for line in answer])
