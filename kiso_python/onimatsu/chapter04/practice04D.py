# -*- coding: utf-8 -*-

customers = [('田中一郎', 25), ('山田太郎', 23),('佐藤花子', 15), ('猫山五郎', 33),\
('小林直子', 26), ('大木虎夫', 18)]

names = [customer[0] for customer in customers if customer[1] >= 20]
print(names)