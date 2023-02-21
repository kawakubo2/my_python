numbers = (10, 20, 30, 40, 50)

for n in numbers:
    print(n)

print(numbers[2])

num = 5
num = 6
print(id(5))
print(id(num))

colors_list = ['赤', '黒', '緑']
colors_tuple = tuple(colors_list)

# colors_tuple[0] = '青'
colors_list[0] = '青';
colors_list.append('白')

print(colors_list)

youbi = '日月火水木金土'

print('今日は' + youbi[3] + '曜日')

for c in youbi:
    print(c + '曜日')

for c in youbi:
    print(c + 'の文字コードは' + str(ord(c)))

print(len('叱る'))
print(len('�る�'))
