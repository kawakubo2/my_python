# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 19:22:56 2017

@author: tomok
"""

import json

# 辞書型
data = {
        "no": 5, #数値
        "code": ("jas", 1, 19), # タプル
        "scr": "be quick to listen, slow to speak, slow to anger", # 文字列
}

# ファイルへ書き込む
filename = "test.json"
with open(filename, "w", encoding="utf-8") as fp:
    json.dump(data, fp)

# ファイルから読み込む
with open(filename, encoding="utf-8") as fp:
    r = json.load(fp)
    print("no=", r['no'])
    print("code=", r['code'])
    print("scr=", r['scr'])
