import random

janken = ['グー', 'チョキ', 'パー']

def judge(player_hand, computer_hand):
    player_pos = janken.index(player_hand)
    computer_pos = janken.index(computer_hand)
    if (player_pos + 1) % 3 == computer_pos:
        return 1
    elif player_pos == computer_pos:
        return 0
    else:
        return -1

for n in range(10):
    player = janken[random.randrange(len(janken))]
    computer = janken[random.randrange(len(janken))]
    j = judge(player, computer)
    print("プレイヤー: {} コンピュータ: {}".format(player, computer))
    if j == 1:
        print("プレイヤーの勝ち")
    elif j == -1:
        print("コンピュータの勝ち")
    else:
        print("引き分け")