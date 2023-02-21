import random

gen = (random.random() for i in range(10))
print('1回目')
for num in gen:
    print(num)

gen = (random.random() for i in range(10))
print('2回目')
for num in gen:
    print(num)
