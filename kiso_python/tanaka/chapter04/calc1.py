import sys

ganpon = int(sys.argv[1])
risoku = float(sys.argv[2])
year = int(sys.argv[3])

result = ganpon
for i in range(year):
    result *= (1 + risoku)
    
print(f"元本{ganpon}万円で1年間の利息が{risoku}%なら{year}年後は{result:.1f}万円になります。")