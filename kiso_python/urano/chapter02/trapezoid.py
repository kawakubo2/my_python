# trapezoid.py

joutei = float(input('上底を入力してください: '))
katei = float(input('下底を入力してください: '))
takasa = float(input('高さを入力してください: '))

menseki = (joutei + katei) * takasa / 2
print('面積: ' + str(menseki))