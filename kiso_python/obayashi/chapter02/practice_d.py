import random

janken = ["グー", "チョキ", "パー"]

a_index = random.randrange(len(janken))
b_index = random.randrange(len(janken))
a = janken[a_index]
b = janken[b_index]

print(f"aさんの手:{janken[a_index]}")
print(f"bさんの手:{janken[b_index]}")
if (a_index + 1) % 3 == b_index:
    print('aさんの勝ち')
elif a_index == b_index:
    print('引き分け')
else:
    print('bさんの勝ち')
