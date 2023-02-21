import sys

if len(sys.argv) < 2:
    print('引数を入力してください')
    sys.exit()

total = 0
for i in range(1, len(sys.argv)):
    total += float(sys.argv[i])

print(f"平均: {total / (len(sys.argv) - 1):.3f}")