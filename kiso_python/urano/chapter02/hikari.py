unit = int(input('時間単位: 1.分 2.時 3.日 : '))

if unit == 1:
    kyori = 300_000 * 60
elif unit == 2:
    kyori = 300_000 * 60 * 60
elif unit == 3:
    kyori = 300_000 * 60 * 60 * 24
else:
    print('1～3を選択してください')

print('距離: ' + str(kyori) + 'km')