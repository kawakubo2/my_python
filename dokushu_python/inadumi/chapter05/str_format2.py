import locale

print('文字列のデフォルトは左揃え、数値は右揃え')
print('|{0:>10}|\n|{0:<10}|'.format('wings'))
print('|{0:*>10}|\n|{0:*<10}|'.format('wings'))
print('|{0:010}|'.format(-12345))
print('|{0:<10}|'.format(-12345))

# TODO 失敗
# locale.setlocale(locale.LC_ALL, 'de_DE')

print('{0:_}'.format(987654321))

n1 = 123_456_789
n2 = 987654321
print('n1=', n1)
print('n2=', n2)

print('{0:#_x}'.format(0x5f5bce1aa))
print('{0:_x}'.format(0x5f5bce1aa))
print('{0:.1f}'.format(5))
print('{0:.5g}g'.format(122.5678))
print('{0:x}'.format(65535))
print('{0:X}'.format(65535))
print('{0:.2%}'.format(23.12345))

s1 = 'こんにちは'
b1 = s1.encode('sjis')
print(len(b1))
s2 = b1.decode('sjis')
print(s2)

