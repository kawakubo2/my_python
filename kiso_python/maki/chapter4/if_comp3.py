# -*- coding: utf-8 -*-

names = [('田中一郎', '男', 56), ('山田太郎', '男', 28), ('佐藤花子', '女', 35),
         ('猫山五郎', '男', 44), ('小林直子', '女', 58), ('大木虎夫', '男', 33)]

men = [n[0] for n in names if n[1] == '男' and n[2] <= 35]
print(men)