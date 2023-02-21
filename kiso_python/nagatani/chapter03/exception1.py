import re, sys

input_str = input('点数を入力してください: ')
pattern = re.compile(r'^\d+$')
result = pattern.search(input_str)
if result:
    score = int(input_str)
else:
    print('整数を入力してください')
    sys.exit()