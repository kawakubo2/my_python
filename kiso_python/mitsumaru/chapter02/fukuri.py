ganpon = int(input('元本(万円)を入力してください: '))
nenri = float(input('年利: '))
kikan = int(input('年数: '))

result = ganpon

for i in range(kikan):
    result *= (1 + nenri)

print(str(kikan) + '後は' + str(result) + '万円となります。')
