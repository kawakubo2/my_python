import random

janken = ["グー", "チョキ", "パー"]
player_index = random.randrange(len(janken))
comp_index = random.randrange(len(janken))
print(f"[プレイヤー]: {janken[player_index]} [コンピュータ]: {janken[comp_index]}")
if (player_index + 1) % 3 == comp_index:
    print("プレイヤーの勝ち")
elif player_index == comp_index:
    print("引き分け")
else:
    print("プレイヤーの負け")