list27 = [ 2, 7, 18, -5, -7, 8, 10, 4 ]

# 上記リストの合計
print(f"合計: {sum(list27)}")

total = 0
for n in list27:
    total += n
    
print(f"合計: {total}")

# 上記リストの内、プラスの数値の合計
total = 0
for n in list27:
    if n > 0:
        total += n
        
print(f"プラスの値の合計: {total}")

# 上記リストの内、偶数だけの合計
total = 0
for n in list27:
    if n % 2 == 0:
        total += n
        
print(f"偶数の合計: {total}")

# 上記リストの内、プラスの偶数の合計

total = 0
for n in list27:
    if n > 0 and n % 2 == 0:
        total += n
        
print(f"プラスの偶数の合計: {total}")
    