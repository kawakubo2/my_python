list26 = [5, 12.3, 'abc', True, 7, -3.4, 10, 'xyz']

# 上記リストから数値型(int, float)の値だけを表示したい
for elem in list26:
    if type(elem) in (int, float):
        print(elem)

# 上記リストから数値型の値の合計を表示したい
total = 0
for elem in list26:
    if type(elem) in (int, float):
        total += elem
        
print(f"合計: {total:.3f}")
