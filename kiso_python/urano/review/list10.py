numbers = [48, 18, 78, 62, 50, 66, 90, 68, 71, 92]

# 50～80の範囲に含まれる数値の合計
total = 0
for n in numbers:
    if 50 <= n <= 80:
        total += n
        
print(f"50～80の範囲にある数値の合計: {total}")