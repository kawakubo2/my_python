list9 = [ 8.3, 13.5, 'A', 7.8, 4.9, 'C', 'D', 10.1, 5.4]

# 数値だけの合計
total = 0
for n in list9:
    if type(n) in (int, float):
        total += n

print(f"合計: {total}")