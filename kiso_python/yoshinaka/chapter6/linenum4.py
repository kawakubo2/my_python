with open('sample.txt', 'r', encoding='utf_8') as f:
    # 糖衣構文(シンタックスシュガー)
    for i, line in enumerate(f, start=1):
        print('{:4d}: {}'.format(i, line.rstrip('\n')))


f = open('kakugen.txt', 'r', encoding='utf_8')
i = 1
while True:
    try:
        line = next(f)
        print('{:4d}: {}'.format(i, line.rstrip('\n')))
        i += 1
    except:
        break