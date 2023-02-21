names = ["田中一郎-1979", "山田花子-2000", "井上太郎-1964",
         "藤本和雄-1988", "大津徹-1959", "後藤信-1980"]

def get_year(s):
    year = s[-4:]
    return int(year)

names.sort(key=lambda s: int(s[-4:]))
print(names)