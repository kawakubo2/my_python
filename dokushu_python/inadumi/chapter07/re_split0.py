import re

ptn = re.compile(r'[/\.-]')

date_list = ['1988-12-31', '2001/1/3', '1999.9.12']

for d in date_list:
    result = ptn.split(d)
    print(result)
    if len(result) != 3:
        print('日付の形式に誤りがあります')
    else:
        print("{}年{}月{}日".format(result[0], result[1], result[2]))