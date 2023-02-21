# regexp_trainer.py
import re

while True:
    pattern = input('正規表現:(終了はq): ')
    if pattern == 'q':
        break
    regexp = re.compile(pattern)
    while True:
        target = input('対象文字列:正規表現に戻るにはq): ')
        if target == 'q':
            break
        result = regexp.search(target)
        if result:
            print('○')
        else:
            print('×')