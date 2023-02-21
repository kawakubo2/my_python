# -*- coding: utf-8 -*-

names = ["田中一郎-1979", "山田花子-2000", "井上太郎-1964",
         "藤本和雄-1988", "大津徹-1959", "後藤信-1980"]

names.sort(key=lambda str: int(str[-4:]))
print(names)

names = ["田中一郎-50", "山田花子-23", "井上太郎-124",
         "藤本和雄-81", "大津徹-70", "後藤信-8"]

names.sort(key=lambda str: int(str.split('-')[1]), reverse=True)
print(names)
