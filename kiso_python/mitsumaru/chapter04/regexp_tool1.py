import re

pattern = input('正規表現: ')

ptn = re.compile(pattern)

while True:
    target = input('対象文字列(終了はq): ')
    if target == 'q': break
    result = ptn.search(target)

    if result:
        print('○: ', end='')
        print(result.group(0))
    else:
        print('x')

