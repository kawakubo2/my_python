import random

janken = ['グー', 'チョキ', 'パー']
print(janken[random.randrange(len(janken))])

if '月' in '日月火水木金土':
    print('○')

if 'B' not in ['A', 'B', 'C', 'D']:
    print('○')
else:
    print('×')