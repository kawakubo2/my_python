import sys

if len(sys.argv) <= 1:
    print("使用法: python practice04B.py 数値1 数値2 ...")
    print("使用例: python practice04B.py 5.23 7.81 9.09")
    sys.exit()
    
total = 0
for i in range(1, len(sys.argv)):
    total += float(sys.argv[i])
    
print(f"平均: {total / (len(sys.argv) - 1):.3f}")