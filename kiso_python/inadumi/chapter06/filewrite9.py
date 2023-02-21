# -*- coding: utf-8 -*-

print("終了する場合@@@@@を入力してください。")
with open('out2.txt', 'a', encoding='utf_8') as f:
    while(True):
        str = input("文字列:")
        if str == '@@@@@':
            break
        f.write(str + '\n')
    