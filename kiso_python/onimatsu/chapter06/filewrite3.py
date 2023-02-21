# -*- coding: utf-8 -*-

import os, sys, random

"""
python filewrite3.py kuji.tx
            ↑           ↑
        　　sys.argv[0] sys.argv[1]
"""

if len(sys.argv) != 2:
    print('ファイル名をひとつ指定してください。')
    sys.exit()
    
path = sys.argv[1]

if os.path.exists(path):
    if input('上書きしますか?(y/n) : ') != 'y':
        sys.exit()
        
kujis = ['大吉', '中吉', '凶']

with open(path, 'w', encoding='sjis') as f:
    f.write(kujis[random.randrange(len(kujis))] + "\n")