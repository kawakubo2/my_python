import sys

total = 0

for i in range(1, len(sys.argv)):
    total += int(sys.argv[i])

print('合計 =', total)