# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 17:25:04 2017

@author: tomok
"""

import qrcode
# QRコードを生成
img = qrcode.make('https://haru-idea.jp/')
# ファイルを保存
img.save("qrcode-test.png")
