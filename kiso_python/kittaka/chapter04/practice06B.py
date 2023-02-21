import sys

"""      _____________________________
sys.argv | practice06B.py | 5 | 4 | 6 |
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                 0          1   2   3
"""
if len(sys.argv) <= 1:
    print("使用法: python practice06B.py 数値1 数値2 ...")
    print("使用例: python practice06B.py 5 4 6")
    sys.exit()
    
total = 0
for i in range(1, len(sys.argv)):
    total += float(sys.argv[i])
    
print(f"平均: {total / (len(sys.argv) - 1):.3f}")

print(type(sys.argv))