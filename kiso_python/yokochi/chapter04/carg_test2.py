import sys

if len(sys.argv) < 2:
    print('使用法: python carg_test2.py 数値1 数値2 ...')
    print('例: python carg_test2.py 5.3 -4.1 3')
    sys.exit()

total = 0
for i in range(1, len(sys.argv)):
    total += float(sys.argv[i])

print(f'総和: {total}')