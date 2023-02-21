# practice_d.py

import random

janken = ['グー', 'チョキ', 'パー']
print(janken[random.randrange(len(janken))])

# listから要素をランダムに取り出すにはrandom.choiceでも可
print(random.choice(janken))