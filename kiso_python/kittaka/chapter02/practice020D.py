import random

janken = ["グー", "チョキ", "パー"]

playerindex = int(input("0:グー 1:チョキ 2:パー : "))
compindex = random.randrange(len(janken))
print(f"プレイヤー: {janken[playerindex]} コンピュータ: {janken[compindex]}")

if (playerindex + 1) % 3 == compindex:
    print("プレイヤーの勝ち")
elif playerindex == compindex:
    print("引き分け")
else:
    print("プレイヤーの負け")

