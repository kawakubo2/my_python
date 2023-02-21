list33 = [100, 'abc', '200', True, 50, 200]

#
# 数値の合計: 350
#

total = 0
for elem in list33:
    if type(elem) in (int, float):
        total += elem
        
print(f"合計: {total}")