a = 10
b = 8

if a > b:
    print('aはbより大きい')
else:
    print('aはb以下')

numbers = [3, 0, 2, 1, 6]

n = -1 
if n in numbers:
    print(f'{n}はリストに存在します')
else:
    print(f'{n}はリストに存在しません')

error_msg = 'xxxは必須入力です。'

error_msg = error_msg or '特になし' # 短絡評価(ショートカット評価)
print(error_msg)

n = 5
n = n and 10
print(f'n={n}')


def get_total(nums):
    total = 0
    for n in nums:
        total += n
    return total

print(get_total(numbers))

itr = iter(numbers)
try:
    while True:
        print(next(itr))
except:
    pass

# Syntax Sugar(糖衣構文)
for n in numbers:
    print(n)