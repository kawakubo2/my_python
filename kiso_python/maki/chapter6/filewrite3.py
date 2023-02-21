# -*- coding: utf-8 -*-

import os, sys, random

# 引数が一つであることを確認
# python3 filewrite3.py abc.txt
#              ↑           ↑
#         sys.argv[0]   sys.argv[1]
if len(sys.argv) != 2:
    print('ファイル名をひとつ指定してください')
    sys.exit()

# 絶対パス /home/ユーザ名/Desktop/
# 相対パス ../brother/xxx.py
path = sys.argv[1]

if os.path.exists(path):
    if input('上書きしますか?(y/n) : ') != 'y':
        sys.exit()

kujis = ['大吉', '中吉', '凶']
with open(path, "w", encoding="utf_8") as f:
    f.write(kujis[random.randrange(len(kujis))] + "\n")