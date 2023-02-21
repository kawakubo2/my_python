sports = ['サッカー', '野球', 'テニス', '水泳', '柔道']
sports.append('バスケットボール')
sports[2] = 'バレーボール'

print(sports)

for s in sports:
    print(s)

# オブジェクトを指定する削除の方法
sports.remove('バレーボール')
print('--------------------')
for s in sports:
    print(s)

# インデックスが分かる場合の削除の方法
del sports[1]
print('--------------------')
for s in sports:
    print(s)

members = ['山田', '田中', '鈴木', '山田', '佐藤', '佐々木', '山田', '斉藤']

print('inで存在するか調べながら削除')
while '山田' in members:
    members.remove('山田')

for m in members:
    print(m)

members2 = ['山田', '田中', '鈴木', '山田', '佐藤', '佐々木', '山田', '斉藤']
print('リストの内包表記を使って削除')
members3 = [m for m in members if m != '山田']
for m in members3:
    print(m)
    
members4 = ['山田', '田中', '鈴木', '山田', '横田', '上田', '佐藤', 
            '佐々木', '山田', '斉藤']

members5 = [m for m in members4 if '田' in m]
print('名前に「田」が付く人のリスト')
for m in members5:
    print(m)
    
members5 = [m for m in members4 if m.find('田') >= 0]
print('名前に「田」が付く人のリスト')
for m in members5:
    print(m)

print('名前の2文字目に「田」が付く人のリスト')
members5 = [m for m in members4 if m[1] == '田']
for m in members:
    print(m)
    
members6 = ['山田', '藤田', '鈴木', '遠藤', '横田', '加藤', '佐藤', 
            '後藤田', '藤岡', '斉藤']

print('名前が「藤」で終わる人のリスト(endswithを使用する方法)')
members7 = [m for m in members6 if m.endswith('藤')]
for m in members7:
    print(m)

members6 = ['山田', '藤田', '鈴木', '遠藤', '横田', '加藤', '佐藤', 
            '後藤田', '藤岡', '斉藤']

print('名前が「藤」で終わる人のリスト(インデックスを指定する方法)')
members7 = [m for m in members6 if m[-1] == '藤']
for m in members7:
    print(m)
