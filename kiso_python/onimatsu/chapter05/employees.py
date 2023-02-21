# -*- coding: utf-8 -*-

employees = [('山田太郎', '課長'), ('横山花子', '部長'), ('田中一郎', '主任'),
             ('山本久美子', '本部長'), ('鈴木次郎', '課長'), ('星山裕子', '主任')]

rank = ['本部長', '部長', '課長', '主任']

for employee in sorted(employees, key=lambda e: rank.index(e[1])):
    print("{}:{}".format(employee[0], employee[1]))
    
rectangles = [(5, 3), (2, 3), (10, 4), (6, 3), (1, 2), (4, 2)]

for rectangle in sorted(rectangles, key=lambda r: r[0] * r[1], reverse=True):
    print("幅:{} 高さ:{}".format(rectangle[0], rectangle[1]))
    
