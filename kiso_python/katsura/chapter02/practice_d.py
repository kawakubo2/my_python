import random

janken = ['グー', 'チョキ', 'パー']
print(janken[random.randrange(len(janken))])
print(random.choice(janken))

n = 5
nums = [1, 3, 5, 7, 9]
exists_flag = False
for num in nums:
    if n == num:
        exists_flag = True
        break
if exists_flag:
    print('存在する')


if n in nums:
    print('存在する')