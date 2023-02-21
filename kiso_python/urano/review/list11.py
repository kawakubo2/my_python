list11 = [-5, 9, 13, -6, 20, -3, 5, -1, 10]

# 正の整数だけの合計
total = 0
for n in list11:
    if n > 0:
        total += n

print(f"正の整数の合計: {total}")

# 負の整数だけの合計
total = 0
for n in list11:
    if n < 0:
        total += n
        
print(f"負の整数の合計: {total}")