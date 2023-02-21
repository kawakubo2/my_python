import sys

total = 0
for n in range(1, len(sys.argv)):
    total += n

print(total)

print(sum([1, 2, 3, 4, 5]))

"""
辞書・・・・・・Python, C#
連想配列・・・・JavaScript, PHP
マップ・・・・・Java, JavaScript
ハッシュ・・・・Ruby
"""

x = 11
y = 5
z = x | y
print(z)

dic = {'日': 'Sun', '月': 'Mon', '火': 'Tue', '水': 'Wed', '木': 'Thu', '金': 'Fri', '土': 'Sat'}

for en, ja in dic.items():
    print(f"{ja}:{en}")