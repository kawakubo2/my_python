names = ['田中一郎-1979', '山田花子-2000', '井上翔太-1964',
         '藤本和雄-1988', '大津徹-1959',   '後藤信-1980']

def get_year(str):
    return int(str[-4:])

names.sort(key=get_year)
print(names)