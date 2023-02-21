names = ["田中一郎-1979", "山田花子-2000", "井上太郎-1964",
         "藤本和雄-1988", "大津徹-1959", "後藤信-1980"]


names.sort(key=lambda n: int(n[-4:]))
print(names)