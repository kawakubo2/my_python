# -*- coding: utf-8 -*-

import random

#suit=('S','H','D','C')
suit=('♠','♡','♦','♣')
nums=('A','2','3','4','5','6','7','8','9','10','J','Q','K')
pokerhands={'0':'ブタ','1':'ワンペア','2':'ツーペア','3':'スリーカード','4':'ストレート','5':'フラッシュ','6':'フルハウス','7':'フォーカード','8':'ストレートフラッシュ','9':'ロイヤルストレートフラッシュ'}

#カードリスト作成
cards = [(s,n) for s in suit for n in nums]

#カウンター初期化
rank0 = 0
rank1 = 0
rank2 = 0
rank3 = 0
rank4 = 0
rank5 = 0
rank6 = 0
rank7 = 0
rank8 = 0
rank9 = 0

for ix in range(100000):
    #カードを配る
    set_cards=set()
    random_value=0
    
    while len(set_cards) < 5:
        random_value=random.randint(0,51)
        set_cards.add(random_value)
    list_cards=list(set_cards)
    list_cards.sort()
    player1_cards=[cards[list_cards[0]],cards[list_cards[1]],cards[list_cards[2]],cards[list_cards[3]],cards[list_cards[4]]]
    
    
    #スート（トランプのマーク）の集計
    spades_count=0
    herts_count=0
    diamonds_count=0
    clubs_count=0
    for i,j in player1_cards:
        if i == suit[0]:
            spades_count += 1
        elif i == suit[1]:
            herts_count += 1
        elif i == suit[2]:
            diamonds_count += 1
        elif i == suit[3]:
            clubs_count += 1
    
    #print('♠:{} ♡:{} ♦:{} ♣:{}'.format(spades_count,herts_count,diamonds_count,clubs_count))
    
    def Get_PokerHands(tmp_cards):
        tmp1 = []
        cnv_num = 0 #絵札のコンバート用
        pre_num = 0 #1つ前のリストの数字を格納                   
        for s,n in tmp_cards:
            if n == 'A':
                cnv_num=1
            elif n == 'J':
                cnv_num=11
            elif n == 'Q':
                cnv_num=12
            elif n == 'K':
                cnv_num=13
            else:
                cnv_num=int(n)
            tmp1.append(cnv_num)
        tmp1.sort()
        for idx,val in enumerate(tmp1):
            if idx==0:
                pre_num=val
                straight_flg = True
            else:
                if val - pre_num == 1:
                    pre_num = val
                else:
                    straight_flg = False

        tmp_set1=set(tmp1) #数字のペアチェック
        tmp_list1=list(tmp_set1) 
        
        hands_rank='0'
        
        if len(tmp_set1) == 2:
            if tmp1.count(tmp_list1[0]) in (2,3):
                hands_rank='6'
            else:
                hands_rank='7'
        
        if len(tmp_set1) == 3:
            if tmp1.count(tmp_list1[0]) == 1:
                if tmp1.count(tmp_list1[1]) == 1:
                    hands_rank='3'
                else:
                    hands_rank='2'
            elif tmp1.count(tmp_list1[0]) == 2:
                hands_rank='2'
            else:
                hands_rank='3'
        
        if len(tmp_set1) == 4:
            hands_rank='1'
        
        if len(tmp_set1) == 5 and straight_flg == True:
            hands_rank='4'
        
        if 5 == spades_count or 5 == herts_count or 5 == diamonds_count or 5 == clubs_count:
            hands_rank = '5'
#            if tmp_cards[0] == 'A' and tmp_cards[1] == '10' and tmp_cards[2] == 'J' and tmp_cards[3] == 'Q' and tmp_cards[4] == 'K' :
            if tmp1[0] == 1 and tmp1[1] == 10 and tmp1[2] == 11 and tmp1[3] == 12 and tmp1[4] == 13 :
                hands_rank = '9'
            elif straight_flg == True:
                hands_rank='8'

        return hands_rank
    
    getrank = Get_PokerHands(player1_cards)
    
    if getrank not in ('0','8','9'):
        player1_cards.sort(key=(lambda player1_cards:player1_cards[1]))
    
# =============================================================================
#     if getrank=='9':
#         print('{}{}{}{}{}:{}'.format(player1_cards[0],player1_cards[2],player1_cards[4],player1_cards[3],player1_cards[1],pokerhands[getrank]))
#     elif getrank in ('4','7','8'):
#         print('{},{},{},{},{}:{}'.format(id(player1_cards[0]),id(player1_cards[1]),id(player1_cards[2]),id(player1_cards[3]),id(player1_cards[4]),pokerhands[getrank]))
#         print('{}{}{}{}{}:{}'.format(player1_cards[0],player1_cards[1],player1_cards[2],player1_cards[3],player1_cards[4],pokerhands[getrank]))
# 
# =============================================================================
# =============================================================================
#     if getrank not in ('0','1'):
#         print('{}{}{}{}{}:{}'.format(player1_cards[0],player1_cards[1],player1_cards[2],player1_cards[3],player1_cards[4],pokerhands[getrank]))
# 
# =============================================================================

    if getrank == '0':
        rank0 += 1
    if getrank == '1':
        rank1 += 1
    if getrank == '2':
        rank2 += 1
    if getrank == '3':
        rank3 += 1
    if getrank == '4':
        rank4 += 1
    if getrank == '5':
        rank5 += 1
    if getrank == '6':
        rank6 += 1
    if getrank == '7':
        rank7 += 1
    if getrank == '8':
        rank8 += 1
    if getrank == '9':
        rank9 += 1
        
print('{}:{},{}:{},{}:{},{}:{},{}:{},{}:{},{}:{},{}:{},{}:{},{}:{}'.format(
    pokerhands['0'],rank0,pokerhands['1'],rank1,pokerhands['2'],rank2,pokerhands['3'],rank3,
    pokerhands['4'],rank4,pokerhands['5'],rank5,pokerhands['6'],rank6,pokerhands['7'],rank7,
    pokerhands['8'],rank8,pokerhands['9'],rank9))







