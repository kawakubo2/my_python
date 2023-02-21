import os, sys

if len(sys.argv) != 3:
    print('使用法: python search1.py 検索文字列 検索対象ファイル')
    print('使用例: python search1.py print linenum2.py')
    sys.exit()

word = sys.argv[1]
filename = sys.argv[2]

if not os.path.exists(os.path.join(os.path.dirname(__file__),filename)):
    print(f'{filename}は存在しません')
    sys.exit()

with open(os.path.join(os.path.dirname(__file__),filename), 'r', encoding='UTF-8') as f:
    for count, line in enumerate(f):
        if word in line:
            print(f'{count+1:4d}: {line}', end='')
