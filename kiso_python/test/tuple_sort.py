# -*- coding: utf-8 -*-

members = [('山田太郎', 170, 70),('田中次郎', 170, 65),\
           ('鈴木三郎', 170, 80),('佐藤四郎', 170, 75)]

members_bmi = sorted(members,\
            key=lambda m: m[2]/(m[1]/100)**2)

for m in members_bmi:
    print(m)