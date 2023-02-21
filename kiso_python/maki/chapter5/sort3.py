# -*- coding: utf-8 -*-

names = ["田中一郎-1979", "山田花子-2000", "井上太郎-1964",
         "藤本和雄-1988", "大津徹-1959", "後藤信-1980"]

def get_year(str):
    year = str[-4:]
    return int(year)

names.sort(key=get_year)
print(names)