# -*- coding: utf-8 -*-
import os
import random
from time import sleep
# import xlrd
import 
wb = xlrd.open_workbook(os.path.dirname(__file__) + '/sample.xlsx')
print()
print('タイピング練習しながら英単語を覚えましょう！')
print('正しく入力されると日本語訳が出ます。')
print('もう覚えた単語はスペースを入力すると次から出題されません。')
print('入力モードは半角英数にしてください。')
print()

levels = ['TOEIC頻出単語101',
'TOEFL頻出単語100',
'TOEIC頻出英単語・熟語集　400点コース',
'TOEIC頻出英単語・熟語集　550点コースその1',
'TOEIC頻出英単語・熟語集　550点コースその2',
'TOEIC頻出英単語・熟語集　550点コースその3',
'TOEIC頻出英単語・熟語集　700点コース',
'TOEIC頻出英単語・熟語集　850点コース']

courses = ['コースA',
'コースB',
'コースC',
'コースD',
'コースE',
'コースF',
'コースG',
'コースH',
'コースI',
'コースJ']

def japanese(ja):
    print(ja)
    print()
    sleep(1)

for i, level in enumerate(levels):
    print('{}.{}'.format(i+1, level))
          
print() 
sheet = wb.sheet_by_name('Sheet' + str(int(input('1~8 の中から選択してください: '))))
print() 
all_en = sheet.col_values(1)
all_jp = sheet.col_values(2)
if sheet == wb.sheet_by_name('Sheet1') or sheet == wb.sheet_by_name('Sheet2'):
    en = all_en
    jp = all_jp
else:
    for i, course in enumerate(courses):
        print('{:2d}.{}'.format(i+1, course))
    print()
    n = int(input('1~10 の中から選択してください: '))
    print()
    en = all_en[n-1::10]
    jp = all_jp[n-1::10]
sleep(1)
print('3')
sleep(1)
print('2')
sleep(1)
print('1')
sleep(1)
print('スタート！')
print()
sleep(1)
while(True):
# =============================================================================
#     if len(en) == 0:
#         break
# =============================================================================
    ran = random.randint(0,len(jp) - 1)
    tango = en[ran]
    print(tango)
    nyuryoku = input()
    if nyuryoku == ' ':
        oboeta = jp[ran]
        en.remove(en[ran])
        jp.remove(jp[ran])
        if len(en) != 0:
            print(tango + ':' + oboeta + '\nは、以降出題されません。')
            print('覚える単語は、あと' + str(len(en)) + '語だよ！')
            print()
            sleep(1)
        elif len(en) == 0:
            print('全部覚えたよ！')
            break
    else:
        if tango == nyuryoku:
            japanese(jp[ran])
            continue
        else:
            while(True):
                print('タイピング頑張れ！！')
                print()
                sleep(1)
                print(tango)
                nyuryoku = input()
                if tango == nyuryoku:
                    japanese(jp[ran])
                    break

            

