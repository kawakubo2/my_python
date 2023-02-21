# -*- coding: utf-8 -*-

print('ファイルへ書き込みます。終了するにはxxを入力してください。')

with open('file1.txt', 'w', encoding='utf_8') as f:
    while True:
        str = input(' > ')
        if str == 'xx':
            break
        f.write(str)
        f.write("\n")