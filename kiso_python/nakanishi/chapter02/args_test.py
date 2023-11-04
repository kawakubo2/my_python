# args_test.py
import sys
if len(sys.argv) != 3:
    print("使用法: python args_test.py 5 8")
    sys.exit(1)
    
answer = float(sys.argv[1]) + float(sys.argv[2])
print("答え: " + str(answer))