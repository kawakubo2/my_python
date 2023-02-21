# -*- coding: utf-8 -*-
import sys

if len(sys.argv) < 2:
    print('引数を指定してください')
    sys.exit()
    
with open('out.txt', 'w', encoding='utf_8') as out_f:
    for i in range(len(sys.argv) - 1):
        out_f.write(sys.argv[i + 1] + '\n')