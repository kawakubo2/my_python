def my_sum(nums):
    total = 0
    for n in nums:
        total += n

if my_sum([1, 2, 3, 4, 5]) is None:
    print('none')

n = 10
if n > 5:
    msg = "合格"
else:
    msg = "不合格"
print(msg)

m = 10
msg = "合格" if m > 5 else "不合格"
print(msg)

msg = 'Hello'
msg = msg or '特になし'
print(msg)

def get_xxx():
    return False
lst = get_xxx() or []
print(lst)

x = 75

if x >= 50 and x <= 100:
    print('○')
else:
    print('×')

if 50 <= x <= 100:
    print('○')
else:
    print('×')

from dis import dis

# dis('50 <= x <= 100')
# print('----------')
# dis('x >= 50 and x <= 100')

x = 0b10
y = 0b11
z = x * y
print(z)

x = 0.2
y = 0.6
print(x * 10 * 3 == y * 10)