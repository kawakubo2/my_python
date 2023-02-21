# -*- coding: utf-8 -*-

employees = [('山田太郎', '課長'), ('横山花子', '本部長'), ('田中一郎', '主任'),
             ('山本久美子', '主任'), ('鈴木次郎', '部長'), ('星山裕子', '主任')]

# 本部長,部長,課長,主任

rank = ['本部長', '部長', '課長', '主任']

for employee in sorted(employees, key=lambda e: rank.index(e[1])):
    print("{}:{}".format(employee[0], employee[1]))
    
trapezoids = [(2.5, 4.78, 3.53), (1.5, 3.42, 2.3), (6.2, 5.3, 2.54),
          (4.23, 5.1, 9.2), (7.21, 8.213, 5.8)]

for t in sorted(trapezoids,\
    key=lambda t: (t[0] + t[1]) * t[2] / 2):
    print("{}:{:.2f}".format(t, (t[0] + t[1]) * t[2] / 2))