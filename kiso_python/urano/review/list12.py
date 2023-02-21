list12 = [ 12, 8, -7, 7, 5, 6, -2, 4, 9, 10]

# 正の偶数の合計
total = 0
for n in list12:
    if n > 0 and n % 2 == 0:
        total += n
        
print(f"正の偶数の合計: {total}")