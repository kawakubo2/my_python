# -*- coding: utf-8 -*-

rank = {'部長': 1, '課長': 2, '主任': 3}

employees = [('田中一郎', '課長'),('山田太郎', '主任'),('佐藤花子', '部長'),
             ('猫山五郎', '課長'),('鈴木理沙', '主任')]

e2 = sorted(employees, key=lambda t: rank[t[1]])
print(e2)

rank2 = ['部長', '課長', '主任']

e3 = sorted(employees, key=lambda t: rank2.index(t[1]))
print(e3)