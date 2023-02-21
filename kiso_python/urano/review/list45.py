list45 = ['list40.py', 'list41.py', 'dict20.py', 'dict22.py', 'list42.py']

# list**.pyのようにlistで始まり、.pyで終るファイルだけを表示する
#
# list40.py list41.py list42.py
#
print('---< 文字列操作で解く >---')
for filename in list45:
    if filename.startswith('list') and filename.endswith('.py'):
        print(filename)

print('---< 正規表現を使って解く >---')
import re
pattern = re.compile('^list.+\.py$')
for filename in list45:
    if pattern.match(filename):
        print(filename)