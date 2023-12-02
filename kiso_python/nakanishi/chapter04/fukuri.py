import sys

if len(sys.argv) != 3:
    print("使用法: python fukuri 元本 年")
    print("使用例: python fukuri 30000000 10")    
    sys.exit(-1)

RATE = 0.03
price = int(sys.argv[1])
year  = int(sys.argv[2])    
original = year
for i in range(year):
    price *= (1 + RATE)

print(f"金利が3%の場合、{original}円の定期預金は{sys.argv[1]}年で{price}円になります。")

print(type(sys.argv))