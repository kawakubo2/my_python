# regexp_test.py
import re

while True:
    pattern = input('正規表現: q(終了時) > ')
    if pattern == 'q':
        break
    reg = re.compile(pattern)
    while True:
        target = input('対象文字列: q(正規表現に戻る) > ')
        if target == 'q':
            break
        if result := reg.search(target):
            print('○')
        else:
            print('x')
