import sys

print(sys.argv)

if len(sys.argv) == 1:
    print("少なくとも1つは引数を入力してください。")
    print("使用法: python practice_b.py 数値1 数値2 ...")
    print("使用例: python practice_b.py 52.12 12.34 8.123")
    sys.exit()

total = 0
for i in range(1, len(sys.argv)):
    try:
        total += float(sys.argv[i])
    except:
        print('引数には数値を入力してください')
        sys.exit()

print(f"平均: {total/(len(sys.argv)-1):.3f}")
