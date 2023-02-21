# -*- coding: utf-8 -*-
"""
Spyderエディタ

これは一時的なスクリプトファイルです
"""

"""
BMIの計算
"""

height = float(input("身長をcmで入力してください : "))
weight = float(input("体重をkgで入力してください : "))

bmi = weight / ((height / 100) ** 2)

print("身長{:.1f}cm、体重{:.1f}kgのBMI値は{:.1f}です".format(height, weight, bmi))