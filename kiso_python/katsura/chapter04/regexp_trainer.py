import re

while True:
    pattern = input('正規表現(終了時はq): ')
    if pattern == 'q':
        break
    reg = re.compile(pattern)
    while True:
        target = input('対象文字列(終了時はq): ')
        if target == 'q':
            break
        result = reg.search(target)
        if (result):
            print('○')
        else:
            print('×')
