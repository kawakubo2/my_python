import random

janken = ['グー', 'チョキ', 'パー']
print(janken[random.randrange(len(janken))])
print('要素数')
print(len(janken))
print('0～2までの乱数')
print(random.randrange(3))

print('--- random.choice ---')
print(random.choice(janken))