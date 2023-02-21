import random

count = {'イタリア': 13, 'イギリス': 10, 'ドイツ': 8, 'スペイン': 7, 'フランス': 4}

lines = []
for country, num in count.items():
    lines += [country + '\n'] * num

random.shuffle(lines)

with open('answer.txt', 'w', encoding='utf_8') as f:
    f.writelines(lines)